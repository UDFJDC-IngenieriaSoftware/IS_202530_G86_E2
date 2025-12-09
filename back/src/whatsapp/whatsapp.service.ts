import { Injectable, InternalServerErrorException, Logger } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { AxiosAdapter } from 'src/common/adapters/axios.adapter';
import { TextPayloadInterface } from './interfaces.ts/textPayload.interface';
import { ImageUrlInfo, MessageText, WhatsappResponse } from './interfaces.ts/WsResponse.interface';
import { options } from 'src/common/interfaces.ts/HttpAdapter.interface';
import { ImagesService } from 'src/images/images.service';
import axios from 'axios';
import { States } from './interfaces.ts/states.enum';
import { EstadoEnvio, EstadoRespuesta, presentacion, reminderInterface, TreatementInterface, UserInterface } from './interfaces.ts/user.interface';

@Injectable()
export class WhatsappService {

    private confirmRemind = new Map<number, {State: States, reminder: reminderInterface }>();
    private state: States = States.START;
    public readonly logger = new Logger()
    constructor(
        private readonly http: AxiosAdapter,
        private readonly configService: ConfigService,
        private readonly ImageService: ImagesService,  // Puedes inyectar también un “UserService” para manejar BD
    ) {}

    private readonly headersData: options = {
        headers: {
        Authorization: `Bearer ${process.env.WHATSAPP_API_KEY}`,
        "Content-Type": "application/json",
        },
    };

    private readonly phoneId = '951070524747774';

    async sendMessage(to: string, message: string) {
        const url = `https://graph.facebook.com/v22.0/${this.phoneId}/messages`;
        const data: TextPayloadInterface = { to, message };
        await this.http.postWhatsapp(url, data, this.headersData);
    }

    /** Maneja TODO mensaje entrante — texto, imagen, lo que llegue */
    async handleIncomingMessage(body: WhatsappResponse) {
        const entry = body.entry?.[0];
        const change = entry?.changes?.[0];
        const value = change?.value;

        const message = value?.messages?.[0];
        const from = value?.contacts?.[0]?.wa_id;

        if (!message || !from) {
        console.log("Ignorando evento sin mensaje válido.");
        return;
        }

        if (message.type === 'text') {
            const messageText = message as MessageText;

            if(this.confirmRemind.size > 0 ){
                this.confirmNotifications(messageText, from);
                return; //Evitar que el programa siga
            }

            const text = messageText.text.body.trim();
            await this.handleTextMessage(from, text);
        } if(message.type === 'image'){
            if(this.state != States.CREATE_NOTIFICATION){
                await this.sendMessage(from, `*La imagen que ha enviado no puede ser procesada aun, por favor acceder primero a la opción correspondiente*`);
                return "No se puede procesar la imagen aun"
            }
            await this.createNotification(from, message);
        }
        else {
            console.log("Tipo de mensaje no manejado", message.type);
        }
    }

    /** Procesa mensajes de texto según estado del usuario / lógica de bot */
    private async handleTextMessage(from: string, text: string) {
        if(this.state != States.START){
            console.log("Se reiniciara")
            await setInterval(()=>{
                console.log("Se reinicio el estado a INICIADO")
                this.state = States.START;
            },300000) //Volver a inicializar el usuario cada 5 minutos
        }

        //Validar que usuario exista en la base de datos si no existe, registrarlo y el estado pasa a register
        console.log(`${this.configService.get('URL_PATIENT')}${from}`)
        if(this.state === States.START){
            const user = await this.http.get<UserInterface|{status:number}>(`${this.configService.get('URL_PATIENT')}${from}`);
            if("status" in user && user.status === 404){
                let text = "Bienvenido a WhatsPills, hemos buscado y al parecer no te encuentras registado en Whatpills, por favor indiquenos la siguiente información:"
                text += "\n- Primer nombre: \n";
                text += "- Segundo nombre: \n";
                text += "- Primer apellido: \n";
                text += "- Segundo apellido: \n";
                text += "- Cedula de ciudadania: \n";
                text += "- Fecha de nacimiento (Año-Mes-Dia):"
                await this.sendMessage(from, text)
                this.state = States.REGISTER_USER
                return "Estado cambiado a registro de usuario";
            }
        }

        if(this.state === States.REGISTER_USER){
            console.log(text)
            const data = text.split("\n")
            let userData: UserInterface = {
                name: data[0],
                second_name: data[1],
                first_lastname: data[2],
                second_lastname: data[3],
                cedula: data[4],
                date_of_birth: new Date(data[5]),
                phone: from
            }
            await this.http.post(this.configService.get('URL_PATIENT')!, userData)
            this.state = States.MENU
        }
        const noWaitingOption: boolean = (
            this.state != States.MENU_WAITING_OPTION && 
            this.state != States.CREATE_CARER &&
            this.state != States.CREATE_MANUALLY_NOTIFICATION &&
            this.state != States.CREATE_NOTIFICATION &&
            this.state != States.EDIT_DELETE_NOTIFICATION
            )
        const user = await this.http.get(`${this.configService.get('URL_PATIENT')}${from}`)
        if(noWaitingOption && user ){
            this.state = States.MENU
        }
        //Si existe enviar opciones, 
        if(this.state === States.MENU){
            
            let text: string = `*Bienvenido a Whatspills* ${user.name} por favor seleccione una de las siguientes opciones para continuar:\n`;
            text += "*1* Registrar Cuidador\n";
            text += "*2* Crear notificacion manualmente\n";
            text += "*3* Crear notificacion con imagen\n";
            text += "*4* Editar o eliminar notificacion\n";
            await this.sendMessage(from, text);
            this.state = States.MENU_WAITING_OPTION;
            return "Estado cambiado a espera de seleccion de opcion"
        }
        console.log(this.state)
        if(this.state === States.MENU_WAITING_OPTION){
            const option = text;
                switch (option) {
                    case "1":
                        return await this.showCaretaker(from);

                    case "2":
                        return await this.showNotificationManual(from);

                    case "3":
                        return await this.showNotificationWithImage(from);

                    case "4":
                        return await this.showeditOrDeleteNotification(from);

                    default:
                        await this.sendMessage(from, "Opción no válida. Por favor selecciona *1*, *2*, *3* o *4*.");
                        return;
                }
        }

        if(this.state === States.CREATE_CARER){
            const data = text.split("\n")
            const dataUserCarer:UserInterface = {
                name: data[0],
                second_name: data[1],
                first_lastname: data[2],
                second_lastname: data[3],
                cedula: data[4],
                date_of_birth: new Date(data[5]),
                phone: data[6]
            } 
            await this.createCaretaker(from,dataUserCarer);
        }

        if(this.state === States.CREATE_NOTIFICATION){
            await this.createNotification(from, text) 
        }

        if(this.state === States.CREATE_MANUALLY_NOTIFICATION){
            let arrayData = text.split("\n");
            const validatePresentation = Object.values(presentacion).find(p => {
                return arrayData[7].normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().includes(p)}
            )
            if(!validatePresentation){
                await this.sendMessage(from, `La presentacion debe de ser alguna de las que se mostraron en el mensaje`);
                return 'Esperar denuevo la inscripcion de la notificacion';
            }
            arrayData[7] = validatePresentation;
            const user: UserInterface = await this.http.get<UserInterface>(`${this.configService.get('URL_PATIENT')}${from}`)
                
            const toJsonData: TreatementInterface = {
                cedula: user.cedula, 
                nombreTratamiento: arrayData[0],
                especialidad: arrayData[1],
                fechaInicio: new Date(arrayData[2]), 
                fechaFin: new Date(arrayData[3]),    
                nombreMedicamento: arrayData[4].normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase(),
                dosis: arrayData[5],
                concentracion: arrayData[6],
                presentacion: arrayData[7] as presentacion,
                frecuencia: Number(arrayData[8]),
                reminder: {
                    estadoEnvio: EstadoEnvio.Pendiente,
                    respuestaPaciente: EstadoRespuesta.SinRespuesta,
                    fechaEnvioRecordatorio: new Date(),
                    fechaRespuesta: new Date(),
                    minutosFaltantes: Number(arrayData[8])*60,
                    notas: arrayData[9]
                }
            }
            console.log(toJsonData)
            await this.createNotificationManual(from, toJsonData)
        }

        return;
    }

    /** Procesa mensajes de tipo imagen */
    private async handleImageMessage(from: string, msg: any) {
        const user = await this.http.get<UserInterface|{status:number}>(`${this.configService.get('URL_PATIENT')}${from}`);
        const image = msg.image;
        if (!image?.id) {
        await this.sendMessage(from, "No se encontró la imagen correctamente.");
        return;
        }

        const fileId = image.id;
        // SSRF mitigation: Only allow safe fileId values (UUIDs or Facebook IDs)
        if (!/^[a-zA-Z0-9_-]{10,}$/.test(fileId)) {
           throw new InternalServerErrorException("Invalid fileId format for Meta Graph API");
        }
        const metaUrl = `https://graph.facebook.com/v22.0/${fileId}`;

        try {
        const imageUrl: ImageUrlInfo = await this.http.getWhatsapp(metaUrl, this.headersData);

        const downloadResponse = await axios.get(imageUrl.url, {
            responseType: "arraybuffer",
            headers: {
            Authorization: `Bearer ${this.configService.get('WHATSAPP_API_KEY')}`,
            },
        });

        const buffer = downloadResponse.data;

        const {text, json} = await this.ImageService.getTextToSend(buffer, user.cedula);
        console.log(json.faltantes.treatmentMissing);
        const dataJson: TreatementInterface = {...json.faltantes.treatmentMissing};
        if((dataJson.cedula != user.cedula)){
            await this.sendMessage(from, `Se detecto un documento de identificacion distinto, se realizaron los cambios correspondientes`)
        }
        await this.sendMessage(from, text);

        
        console.log(dataJson);
        return json;
        } catch (error: any) {
        await this.sendMessage(from, "Lo siento, hubo un error procesando la imagen.");
        }
    }



    private async showCaretaker(from: string) {
        let text = "Para registrar un cuidado por favor ingrese la siguiente informacion del mismo:"
        text += "\n- *Primer nombre:* \n";
        text += "- *Segundo nombre:* \n";
        text += "- *Primer apellido:* \n";
        text += "- *Segundo apellido:* \n";
        text += "- *Cedula de ciudadania:* \n";
        text += "- *Fecha de nacimiento (Año-Mes-Dia):*\n"
        text += "- *Telefono:*";
        await this.sendMessage(from, text);
        this.state = States.CREATE_CARER
        return "Estado cambiado a creando cuidador";
    }
    private async showNotificationManual(from: string) {
        let text = "Para crear un nuevo tratamiento manual, por favor ingrese la siguiente información:";
        text += "\n\n- *Nombre del tratamiento:* \n\n";
        text += "- *Especialidad del tratamiento:* \n\n";
        text += "- *Fecha de inicio (Año-Mes-Día):* \n\n";
        text += "- *Fecha de fin (Año-Mes-Día):* \n\n";
        text += "- *Nombre del medicamento:* \n\n";
        text += "- *Dosis del medicamento:* \n\n";
        text += "- *Concentración del medicamento:* \n\n";
        text += "- *Presentacion del medicamento (comprimidos, cápsulas, jarabes, cremas, parches, inyectables o aerosoles):* \n\n";
        text += "- *Frecuencia (ej: cada 8 horas):* \n\n";
        text += "- *Notas u observaciones adicionales:*";
        
        await this.sendMessage(from, text);
        this.state = States.CREATE_MANUALLY_NOTIFICATION;
        return "Estado cambiado a creando notificación manual";
    }
    private async showNotificationWithImage(from: string) {

        let text = "Para crear una notificación a partir de una imagen, por favor envíenos una foto clara de la receta médica.";
        text += "\nAsegúrese de que se vea bien lo siguiente:";
        text += "\n- Nombre del paciente";
        text += "\n- Nombre del medicamento";
        text += "\n- Dosis";
        text += "\n- Frecuencia";
        text += "\n- Indicaciones o notas del médico";
        text += "\n\n Envíe ahora la imagen para continuar.";

        await this.sendMessage(from, text);
        this.state = States.CREATE_NOTIFICATION;
        return "Estado cambiado a creando notificación con imagen";
    }

    private async showeditOrDeleteNotification(from: string) {}



    private async createCaretaker(from, body){
        const result = await this.http.post(`${this.configService.get('URL_CARER')}`,body);
        if(result){
            this.sendMessage(from, `Cuidador creado exitosamente`)
            this.state = States.MENU;
            return "Volviendo al menu"
        }
    }

    private async createNotificationManual(from: string, body: TreatementInterface) {
        //Consultar que el medicamento exista
        const {nombreMedicamento,concentracion,presentacion, ...Data} = body;
        console.log(Data)
        console.log(`${this.configService.get('URL_MEDICINE')}${nombreMedicamento}/${concentracion}/${presentacion}`)
        let medicine = await this.http.get(`${this.configService.get('URL_MEDICINE')}${nombreMedicamento}/${concentracion}/${presentacion}`);
        //Si no se encuentra, se crea la nueva medicina
        if(medicine.status === 404){
            const medicamento = {
                nombreMedicamento,
                presentacion,
                concentracion
            }
            await this.http.post(`${this.configService.get('URL_MEDICINE')}`, medicamento)
            medicine = await this.http.get(`${this.configService.get('URL_MEDICINE')}${nombreMedicamento}/${concentracion}/${presentacion}`);
        }   
        //crear tratamiento y recordatorio
        const tratamiento = {
            cedula_patient: Data.cedula,
            name: Data.nombreTratamiento.trim().toLowerCase(),
            especiality: Data.especialidad,
            dose: Data.dosis,
            frequence: Data.frecuencia,
            start_date: Data.fechaInicio,
            end_date: Data.fechaFin
        }
        await this.http.post(`${this.configService.get('URL_TREATMENT')}`,tratamiento)
        //Obtener id del tratamiento para crear el recordatorio
        const {id_treatment,...data} = await this.http.get(`${this.configService.get('URL_TREATMENT')}${tratamiento.name}/${tratamiento.cedula_patient}`)
        console.log(id_treatment);
        const recordatorio = {
            idMedicamento: medicine.idMedicamento,
            idTratamiento: id_treatment,
            estadoEnvio: body.reminder.estadoEnvio,
            respuestaPaciente: body.reminder.respuestaPaciente,

            fechaEnvioRecordatorio: body.reminder.fechaEnvioRecordatorio,
            minutosFaltantes: body.reminder.minutosFaltantes,
            notas: body.reminder.notas
        }
        console.log(recordatorio)
        await this.http.post(`${this.configService.get('URL_REMINDER')}`,recordatorio);
        this.sendMessage(from, `Se ha creado correactamente su tratamiento, la siguiente notifiacion sonara en: ${recordatorio.minutosFaltantes/60} horas`)
        this.state = States.MENU

    }

    private async createNotification(from: string, message: any) {
        const json = await this.handleImageMessage(from, message);
        console.log(json);
        this.state = States.MENU;
        return "Volviendo al menu";
    }

    public activateReminderConfirm(State: States, reminder: reminderInterface) {
        this.state = States.RECIPE_CONFIRM
        this.setState(State, reminder);
    }

    private setState(State: States, reminder: reminderInterface){
        this.confirmRemind.set(reminder.idRecordatorio!, {reminder, State});
    }

    private unsetState(reminderId){
        this.confirmRemind.delete(reminderId);
    }

    private async confirmNotifications(messageText,from){
        const raw = messageText.text.body.trim().toLowerCase();
        const num = Number(raw);

        //No es un número → pedir uno
        if (isNaN(num)) {
            const lista = [...this.confirmRemind.keys()].join(", ");
            await this.sendMessage(
                from,
                `Por favor escriba el número de la notificación que desea confirmar:\n➡ ${lista}`
            );
            return;
        }

        if (!this.confirmRemind.has(num)) {
            const lista = [...this.confirmRemind.keys()].join(", ");
            await this.sendMessage(
                from,
                `El número ${num} no está pendiente.\nNotificaciones pendientes: ${lista}`
            );
            return;
        }
        const currentReminder = this.confirmRemind.get(num);
        const updateReminder: reminderInterface = {
                ...currentReminder!.reminder,
                estadoEnvio: EstadoEnvio.Pendiente,
                fechaRespuesta: new Date(),
                minutosFaltantes: currentReminder?.reminder.minutosFaltantes!,
                respuestaPaciente: EstadoRespuesta.Confirmado,
        }
        await this.http.put(
            `${this.configService.get('URL_REMINDER')}${num}`,
            {
                ...updateReminder
            }
        );

        this.unsetState(num);

        await this.sendMessage(
            from,
            `Perfecto. Se confirmó la toma del medicamento.`
        );
        this.state = States.START;
        return; 
    }


}
