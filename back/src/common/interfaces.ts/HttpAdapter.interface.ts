import { TextPayloadInterface } from "src/whatsapp/interfaces.ts/textPayload.interface";

export interface HttpAdapter {
    get<T>(url: string, options: options): Promise<T>;
    post<T>(url: string, data: TextPayloadInterface, options: options): Promise<T>;
}

export interface options {
    headers: {
        Authorization: string;
        "Content-Type": string;
    }
}
