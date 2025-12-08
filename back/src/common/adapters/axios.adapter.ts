import axios, { AxiosInstance } from "axios";
import { HttpAdapter, options } from "../interfaces.ts/HttpAdapter.interface";
import { Injectable, InternalServerErrorException, Logger } from "@nestjs/common";
import { TextPayloadInterface } from "src/whatsapp/interfaces.ts/textPayload.interface";

@Injectable()
export class AxiosAdapter implements HttpAdapter {

    private readonly logger = new Logger('HttpAdapter');
    private axios: AxiosInstance = axios;
    async postWhatsapp<T>(url: string, data: TextPayloadInterface, options: options): Promise<T> {

        const payload = {
            messaging_product: "whatsapp",
            recipient_type: "individual",
            to: data.to,
            type: "text",
            text: {
                preview_url: false,
                body: data.message
            }
        };

        try {
            const { data: result } = await this.axios.post(url, payload, {
                headers: {
                    Authorization: options.headers.Authorization,
                    "Content-Type": options.headers["Content-Type"],
                }
            });

            return result;

        } catch (error: any) {
            console.error("❌ AxiosAdapter POST Error:", error.response?.data || error);
            throw new InternalServerErrorException("Error enviando mensaje a WhatsApp API");
        }
    }


    async getWhatsapp<T>(url: string, options: options): Promise<T> {

        try {
            const { data } = await this.axios.get(url, {
                headers: {
                    Authorization: options.headers.Authorization,
                    "Content-Type": options.headers["Content-Type"]
                }
            });

            return data;

        } catch (error: any) {
            console.error("AxiosAdapter GET Error:", error.response?.data || error);
            throw new InternalServerErrorException("Error en petición GET a WhatsApp API");
        }

    }

    async get<T>(url:string){
        try {
            const {data} = await this.axios.get(url)
            return data;
        } catch (error) {
            this.logger.error;
            throw new InternalServerErrorException(`Error en el AxiosAdapter, detalles:${error}`)
        }
    }

}
