import { BadRequestException, Injectable } from '@nestjs/common';
import { finalization } from 'process';
import { GeminiService } from 'src/gemini/gemini.service';
import { EstadoEnvio, EstadoRespuesta, presentacion } from 'src/whatsapp/interfaces.ts/user.interface';

@Injectable()
export class ImagesService {

    constructor(
        private readonly geminiService: GeminiService,
    ){}
    
    async getJsonWithBuffer(buffer: Buffer){
        return await this.geminiService.getJsonFromDataImageBuffer(buffer);
    }

    async getTextToSend(buffer: Buffer, cedula: string): Promise<{text: string, json: {
        receta:
        {paciente:{
                nombre: string,
                identificacion:string 
            },
            medico: {
                nombre: string
            },
            fecha: Date,
            medicamentos: [
                {
                nombre: string,
                dosis: string,
                frecuencia: string,
                duracion: Date
                }
            ],
            notas: string,
        },
        faltantes:{
            treatmentMissing: {
            cedula: string,
            nombreTratamiento: string,
            especialidad: string,
            fechaInicio: Date,
            fechaFin: Date,
            nombreMedicamento: string,
            dosis: string,
            concentracion: string,
            presentacion: presentacion,
            frecuencia: number,
            reminder: {
                idRecordatorio?: number,
                idTratamiento?: number,
                idMedicamento?: number,
                minutosFaltantes: number,
                notas: string,
                estadoEnvio: EstadoEnvio,
                respuestaPaciente: EstadoRespuesta,
                fechaEnvioRecordatorio: Date,
                fechaRespuesta: Date,
                }
            }
        }

        
        }}> {
        const data =  await this.geminiService.getJsonFromDataImageBuffer(buffer);
        let text = `*📄 Resultado de la receta médica OCR*\n\n`;

        text += `*Paciente*\n${data.receta.paciente.nombre}\n${cedula}\n\n`;
        text += `*Médico*\n${data.receta.medico.nombre}\n\n`;
        text += `*Fecha*: ${data.receta.fecha}\n\n`;
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
