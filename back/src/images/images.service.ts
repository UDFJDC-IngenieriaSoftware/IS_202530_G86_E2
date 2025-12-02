import { Injectable } from '@nestjs/common';
import { GeminiService } from 'src/gemini/gemini.service';

@Injectable()
export class ImagesService {

    constructor(
        private readonly geminiService: GeminiService,
    ){}
    
    async getJsonWithBuffer(buffer: Buffer){
        return await this.geminiService.getJsonFromDataImageBuffer(buffer);
    }

    async getTextToSend(buffer: Buffer) {
        const jsonResponse =  await this.geminiService.getJsonFromDataImageBuffer(buffer);
        let text = `*📄 Resultado de la receta médica OCR*\n\n`;

        text += `*Paciente*\n${jsonResponse.paciente.nombre}\n${jsonResponse.paciente.identificacion}\n\n`;
        text += `*Médico*\n${jsonResponse.medico.nombre}\n\n`;
        text += `*Fecha*: ${jsonResponse.fecha}\n\n`;
        text += `*Medicamentos:*\n`;

        jsonResponse.medicamentos.forEach((m, i) => {
            text += `\n${i + 1}. *${m.nombre}*\n`;
            text += `   - Dosis: ${m.dosis}\n`;
            text += `   - Frecuencia: ${m.frecuencia}\n`;
            text += `   - Duración: ${m.duracion}\n`;
        });

        text += `\n*📝 Notas:* ${jsonResponse.notas}`;

        return text;
    }
}
