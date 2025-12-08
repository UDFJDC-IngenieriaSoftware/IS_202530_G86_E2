import { Injectable, InternalServerErrorException, Logger } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { AxiosAdapter } from 'src/common/adapters/axios.adapter';
import { TextPayloadInterface } from './interfaces.ts/textPayload.interface';
import { ImageUrlInfo, MessageText, WhatsappResponse } from './interfaces.ts/WsResponse.interface';
import { options } from 'src/common/interfaces.ts/HttpAdapter.interface';
import { ImagesService } from 'src/images/images.service';
import axios from 'axios';
import { States } from './interfaces.ts/states.enum';

@Injectable()
export class WhatsappService {

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
        return await this.http.postWhatsapp(url, data, this.headersData);
    }

    /** Maneja TODO mensaje entrante — texto, imagen, lo que llegue */
    async handleIncomingMessage(body: WhatsappResponse) {
        console.log(JSON.stringify(body,null, 2));
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
            const text = messageText.text.body.trim();
            await this.handleTextMessage(from, text);
        } else if (message.type === 'image') {
            await this.handleImageMessage(from, message);
        } else {
            console.log("Tipo de mensaje no manejado:", message.type);
        }
    }

    /** Procesa mensajes de texto según estado del usuario / lógica de bot */
    private async handleTextMessage(from: string, text: string) {
        

        //Validar que usuario exista en la base de datos si no existe, registraro y el estado pasa a register
        try {
            const user = await this.http.get(`http://127.0.0.1:8000/patient/${from}`)
            if(!user){
                await this.sendMessage(from, `
                    Bienvenido, hemos buscado y al parecer no se encuentra registado, 
                    por favor indiquenos la siguiente información:
                    \n
                    Primer nombre: \n
                    Segundo nombre (Si aplica): \n
                    Primer apellido: \n
                    Segundo apellido: \n
                    `)
                this.state = States.REGISTER_NAME
            }
        } catch (error) {
            this.logger.error
            throw new InternalServerErrorException(error)
        }
        
        this.state = States.REGISTER_NAME


        // 🚨 Aquí debes integrar tu lógica de usuarios:
        // Ej: const user = await this.userService.getOrCreate(from);
        // switch(user.state) { ... } etc.

        // Por ahora un simple ejemplo de respuesta:
        await this.sendMessage(from, `Me dijiste: "${text}". Gracias por tu mensaje 😊`);
    }

    /** Procesa mensajes de tipo imagen */
    private async handleImageMessage(from: string, msg: any) {
        const image = msg.image;
        if (!image?.id) {
        await this.sendMessage(from, "No se encontró la imagen correctamente.");
        return;
        }

        const fileId = image.id;
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

        const textToSend = await this.ImageService.getTextToSend(buffer);

        await this.sendMessage(from, textToSend);
        } catch (error: any) {
        console.error("❌ Error al procesar imagen:", error.response?.data || error);
        await this.sendMessage(from, "Lo siento, hubo un error procesando la imagen.");
        }
    }
}
