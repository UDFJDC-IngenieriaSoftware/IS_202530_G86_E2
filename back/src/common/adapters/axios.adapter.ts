import axios, { AxiosInstance } from "axios";
import { HttpAdapter, options } from "../interfaces.ts/HttpAdapter.interface";
import { BadRequestException, Injectable, InternalServerErrorException, Logger } from "@nestjs/common";
import { TextPayloadInterface } from "src/whatsapp/interfaces.ts/textPayload.interface";
import { stat } from "fs";

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
            console.error("AxiosAdapter POST Error:", error.response?.data || error);
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
            const Req = await this.axios.get(url)
            return Req.data;    
        } catch (error) {
            return this.handlerErrors(error)
        }
    }

    async post(url: string, body:object) {
        try {
            const result = await this.axios.post(url, body);
            return result;
        } catch (error) {
            return this.handlerErrors(error)
        }
    }

    put(url: string, body: object) {
        try {
            const result = this.axios.put(url,body)
            return result;
        } catch (error) {
        this.handlerErrors(error);       
        }
    }

    private handlerErrors(error){
        this.logger.error(error)
        if(error.response.status === 404){
            return {
                status: 404
            }
        }if(error.response.status === 422){
            return {
                status: 422
            }
        }if(error.response.status === 500){
            return{
                status: 500
            }
        }
    }



}
