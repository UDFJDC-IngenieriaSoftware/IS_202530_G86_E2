import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { AxiosAdapter } from 'src/common/adapters/axios.adapter';
import { TextPayloadInterface } from './interfaces.ts/textPayload.interface';
import { ImageUrlInfo, Message, WhatsappResponse } from './interfaces.ts/WsResponse.interface';
import { options } from 'src/common/interfaces.ts/HttpAdapter.interface';
import { ImagesService } from 'src/images/images.service';
import axios from 'axios';


@Injectable()
export class WhatsappService {
    
    
    
    constructor(
        private readonly http: AxiosAdapter,   
        private readonly configService: ConfigService,
        private readonly ImageService: ImagesService


    ){}
    private readonly headersData: options = {
        headers: {
                authorization: `Bearer ${process.env.WHATSAPP_API_KEY}`,
                content_type: 'application/json'
                }
    }
    
    private readonly phoneId = '951070524747774'; // tu phone number ID

    async sendMessage(to: string, message: string){
        const url = `https://graph.facebook.com/v22.0/${this.phoneId}/messages`;

        const data: TextPayloadInterface= {
            to,
            message
        }
        
        return await this.http.post(url, data, this.headersData);
    }


    async getImage(body: WhatsappResponse){
        // Validar estructura mínima
            const entry = body.entry?.[0];
            const change = entry?.changes?.[0];
            const value = change?.value;

        if (!value?.messages || value.messages.length === 0) {
                console.log("No hay mensajes en este webhook. Posiblemente es un status, ack o evento distinto.");
                return;
            }

            const data = value.messages[0];

            if (data.type !== "image" || !data.image?.id) {
                console.log("El mensaje recibido NO es una imagen");
                return;
            }

            const phoneNumber = value.contacts?.[0]?.wa_id;
            if (!phoneNumber) {
                console.log("No se encontró el número del usuario");
                return;
            }

        //Contruir url para obtener la url de la imagen
        let url = `https://graph.facebook.com/v22.0/${data.image.id}`
        const imageUrl: ImageUrlInfo = await this.http.get(url, this.headersData)

        //Reusar la variable para la url real de la imagen
        url = imageUrl.url

        const response = await axios.get(url, {
            responseType: "arraybuffer",
            headers: {
                Authorization: `Bearer ${this.configService.get('WHATSAPP_API_KEY')}`
            }
        });
        const buffer: Buffer = response.data
        const textToSend = await this.ImageService.getTextToSend(buffer);

        const result = await this.sendMessage(phoneNumber, textToSend);
        console.log(result);
    }
}
