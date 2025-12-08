import { TextPayloadInterface } from "src/whatsapp/interfaces.ts/textPayload.interface";

export interface HttpAdapter {
    getWhatsapp<T>(url: string, options: options): Promise<T>;
    postWhatsapp<T>(url: string, data: TextPayloadInterface, options: options): Promise<T>;
    get<T>(url:string): Promise<T>
}

export interface options {
    headers: {
        Authorization: string;
        "Content-Type": string;
    }
}
