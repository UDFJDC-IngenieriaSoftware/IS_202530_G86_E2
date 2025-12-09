import { BadRequestException, Injectable } from '@nestjs/common';
import { finalization } from 'process';
import { GeminiService } from 'src/gemini/gemini.service';
import { EstadoEnvio, EstadoRespuesta, presentacion, TreatementInterface } from 'src/whatsapp/interfaces.ts/user.interface';
import { RecetaInterface } from './interfaces/recetaBase.interface';

@Injectable()
export class ImagesService {

    constructor(
        private readonly geminiService: GeminiService,
    ){}
    
    async getJsonWithBuffer(buffer: Buffer){
        return await this.geminiService.getJsonFromDataImageBuffer(buffer);
    }

    async getTextToSend(buffer: Buffer, cedula: string): Promise<{text: string, json: {receta: RecetaInterface, faltantes:{treatmentMissing: TreatementInterface} }}> {
        const data =  await this.geminiService.getJsonFromDataImageBuffer(buffer);
        let text = `*📄 Resultado de la receta médica OCR*\n\n`;

        text += `*Paciente*\n${data.receta.paciente.nombre}\n${cedula}\n\n`;
        text += `*Médico*\n${data.receta.medico.nombre}\n\n`;
        text += `*Fecha*: ${data.receta.fechaInicio}\n\n`;
        text += `*Medicamentos:*\n`;

        data.receta.medicamentos.forEach((m, i) => {
            text += `\n${i + 1}. *${m.nombre}*\n`;
            text += `   - Dosis: ${m.dosis}\n`;
            text += `   - Frecuencia: ${m.frecuencia}\n`;
            text += `   - Duración: ${m.duracion}\n`;
        });

        text += `\n*📝 Notas:* ${data.receta.notas}`;
        if(data.receta.status){
            throw new BadRequestException(`No fue posible obtener suficiente informacion de la imagen`);
        }
        return {text, json: {receta: data.receta, faltantes: data.faltantes}};
    }
}
