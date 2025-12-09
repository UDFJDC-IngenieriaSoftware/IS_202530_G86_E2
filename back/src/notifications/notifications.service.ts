import { Injectable, Logger } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { Cron, CronExpression } from '@nestjs/schedule';
import { AxiosAdapter } from 'src/common/adapters/axios.adapter';
import { States } from 'src/whatsapp/interfaces.ts/states.enum';
import { EstadoEnvio, EstadoRespuesta, reminderInterface, UserInterface } from 'src/whatsapp/interfaces.ts/user.interface';
import { WhatsappService } from 'src/whatsapp/whatsapp.service';

@Injectable()
export class NotificationsService {

    private logger = new Logger("NotificacionsService");

    constructor(
        private readonly http: AxiosAdapter,
        private readonly configService: ConfigService,
        private readonly whatsappService: WhatsappService
    ){}

    
    @Cron(CronExpression.EVERY_5_MINUTES)
    async comprobarNotifiacion(){

        //Consultar en la base de datos las notifiaciones
        const recordatorios: reminderInterface[] = await this.http.get(`${this.configService.get('URL_REMINDER')}`);
        recordatorios.forEach(async (reminder) =>{

            reminder.minutosFaltantes -= 5

            //Disminuir el tiempo en minutos en la base de datos
            await this.http.put(`${this.configService.get('URL_REMINDER')}${reminder.idRecordatorio}`,{...reminder})

            //Consultar tratamiento
            const tratamiento = await this.http.get(`${this.configService.get('URL_TREATMENT')}${reminder.idTratamiento}`) 
            const medicine = await this.http.get(`${this.configService.get('URL_MEDICINE')}${reminder.idMedicamento}`);
            //Consultar paciente dueno del tratamiento
            const paciente: UserInterface = await this.http.get(`${this.configService.get('URL_PATIENT')}${tratamiento.cedula_patient}`)
            if(reminder.minutosFaltantes === 0 ){
                let text = `*!!Hola ${paciente.name}¡¡*`;
                text += `\n*Es hora de tomar tu medicamento:*\n\n`;
                text += `Medicamento: ${medicine.nombreMedicamento}\n`
                text += `Dosis: ${tratamiento.dose}\n\n`
                text += `Porfavor confirmar la toma del medicamento escribiendo el numero ${reminder.idRecordatorio}`;
                await this.whatsappService.sendMessage(paciente.phone, text)
                reminder.minutosFaltantes = tratamiento.frequence * 60;//Enviar inicializado el tiempo del recordatorio;
                await this.whatsappService.activateReminderConfirm(States.RECIPE_CONFIRM, reminder)

                const updateReminder: reminderInterface = {
                    ...reminder,
                    estadoEnvio: EstadoEnvio.Enviado,
                    fechaEnvioRecordatorio: new Date(),
                    respuestaPaciente:EstadoRespuesta.SinRespuesta,
                    minutosFaltantes: -1 //No puede volver a iniciar la cuenta hasta que no se haya confirmado la toma del medicamento
                }
                await this.http.put(`${this.configService.get('URL_REMINDER')}${reminder.idRecordatorio}`,{...updateReminder})
            }
        })
    }

}
