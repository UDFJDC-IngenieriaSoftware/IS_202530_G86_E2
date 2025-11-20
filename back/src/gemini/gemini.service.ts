import { GoogleGenAI } from '@google/genai';
import { Injectable } from '@nestjs/common';
import { OcrService } from 'src/ocr/ocr.service';

@Injectable()
export class GeminiService {

    private readonly ai;

    constructor(
        private readonly ocrService: OcrService
    ) {
        this.ai = new GoogleGenAI({
        apiKey: process.env.GEMINI_API_KEY,
        });
    }

    async getJsonFromDataImage(path: string) {
        const imageText = await this.ocrService.readImage(path);

        const prompt = `
        Eres un asistente especializado en estructurar información proveniente de recetas médicas.

        A continuación te entregaré el texto detectado por OCR.  
        Tu tarea es analizarlo y devolver únicamente un JSON válido, sin explicaciones ni texto adicional.

        El JSON debe tener esta estructura:

        {
        "paciente": {
            "nombre": "",
            "identificacion": ""
        },
        "medico": {
            "nombre": ""
        },
        "fecha": "",
        "medicamentos": [
            {
            "nombre": "",
            "dosis": "",
            "frecuencia": "",
            "duracion": ""
            }
        ],
        "notas": ""
        }

        Reglas:
        - Si algún dato no aparece, deja el campo como "".
        - Si hay varios medicamentos, inclúelos en la lista.
        - Interpreta abreviaturas médicas (mg, ml, VO, c/8h, etc.).
        - No inventes información.
        - Devuelve solo el JSON.

        Texto OCR detectado:
        """${imageText.text}"""
        `;
        const result = await this.ai.models.generateContent({
            model: "gemini-2.5-flash",
            contents: prompt,
        });
        const text: string = result.candidates[0].content.parts[0].text;
        const dataJson = JSON.parse(text.replace(/```json/gi, '').replace(/```/g, '').trim());
        return dataJson;
    }

}
