import axios, { AxiosInstance } from "axios";
import { HttpAdapter, options } from "../interfaces.ts/HttpAdapter.interface";
import { Injectable, InternalServerErrorException, Logger } from "@nestjs/common";
import { TextPayloadInterface } from "src/whatsapp/interfaces.ts/textPayload.interface";

@Injectable()
export class AxiosAdapter implements HttpAdapter{

    private readonly logger = new Logger('HttpAdapter');



    
    async post<T>(url: string, data: TextPayloadInterface, options: options): Promise<T> {

        const payload = {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": data.to,
            "type": "text",
            "text": {
                "preview_url": false,
                "body": data.message
            }
        }


        try {
            const {data} = await this.axios.post(url, payload, {
                headers:{
                    Authorization: options.headers.authorization,
                    "Content-Type": options.headers.content_type
                }
            });
            return data;
        } catch (error) {
            console.log(this.logger.error);
            throw new InternalServerErrorException(this.logger.error)
        }
    }
    private axios: AxiosInstance = axios;

    async get<T>(url: string, options: options): Promise<T> {

        try {
            const {data} = await this.axios.get( url,{
                headers:{
                    Authorization: options.headers.authorization,
                    "Content-Type": options.headers.content_type
                }
            });
            return data;
        } catch (error) {
            throw new Error('This is an error - Check logs');
        }

    }

}