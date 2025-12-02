import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { AxiosAdapter } from 'src/common/adapters/axios.adapter';
import { TextPayloadInterface } from './interfaces.ts/textPayload.interface';
import { Message, WhatsappResponse } from './interfaces.ts/WsResponse.interface';
import { options } from 'src/common/interfaces.ts/HttpAdapter.interface';


@Injectable()
export class WhatsappService {
    
    
    
    constructor(
        private readonly http: AxiosAdapter,   
        private readonly configService: ConfigService,



    ){}
    private readonly headersData: options = {
        headers: {
                authorization: `Bearer ${process.env.WHATSAPP_API_KEY}`,
                content_type: 'application/json'
                }
    }
    
    private readonly phoneId = '951070524747774'; // tu phone number ID

    async sendMessage(){
        const message = "hola te estoy hablando desde la api de whatsapp";
        const url = `https://graph.facebook.com/v22.0/${this.phoneId}/messages`;

        const data: TextPayloadInterface= {
            to: "573227790285",
            message
        }
        
        return await this.http.post(url, data, this.headersData);
    }


    async getImage(body: WhatsappResponse){
        const data: Message = body.entry[0].changes[0].value.messages[0]

        //Contruir url para obtener la url de la imagen
        let url = `https://graph.facebook.com/v22.0/${data.image.id}`
        const imageUrl = await this.http.get(url, this.headersData)
        console.log(imageUrl);
        // const data: WhatsappResponse = JSON.stringify(body, null, 2);
        // console.log(data)

        // const imageUrl = await this.http.get('')

    }




    
}
