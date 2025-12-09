import { GoogleGenAI } from '@google/genai';
import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { OcrService } from 'src/ocr/ocr.service';

@Injectable()
export class GeminiService {

    private readonly ai;

    constructor(
        private readonly ocrService: OcrService,
        private readonly configService: ConfigService
    ) {
        this.ai = new GoogleGenAI({
        apiKey: configService.get('GEMINI_API_KEY'),
        });
    }

    async getJsonFromDataImageBuffer(buffer: Buffer){
        const imageText = await this.ocrService.readImageBuffer(buffer);
        const prompt = `
            
            "prompt_optimizacion": {
                "rol": "Eres un asistente especializado en la estructuración de información médica. Tu única tarea es analizar el texto detectado por OCR de una receta médica y devolver exclusivamente JSON válido, sin ningún texto, explicación, preámbulo o nota adicional.",
                "tarea": "Generar dos objetos JSON anidados dentro de una respuesta JSON única.",
                "estructura_respuesta_obligatoria": {
                "receta": "{JSON PRINCIPAL (Receta Médica)}",
                "faltantes": "{JSON DE CAMPOS FALTANTES}"
                },
                "reglas_json_principal": [
                "Estructura obligatoria: { 'paciente': { 'nombre': '', 'identificacion': '' }, 'medico': { 'nombre': '' }, 'fechaInicio': '', 'medicamentos': [ { 'nombre': '', 'dosis': '', 'frecuencia': '', 'duracion': '', 'fechafin': '' } ], 'notas': '' }",
                "Si un dato aparece en el OCR, debe ir en el JSON.",
                "Si un dato falta, déjalo como una cadena vacía (\"\").",
                "Interpretar abreviaturas médicas (ej: mg, ml, VO, c/8h).",
                "La frecuencia debe ser un **número** dado **únicamente en horas** (ej: 8, 12, 24).",
                "Usar 'fechaInicio' como fecha base y calcular 'fechafin' sumando la 'duracion'.",
                "No inventar información.",
                "Aplicar una ligera interpretación (10%) solo si los campos 'nombre'/'dosis'/'notas' son ambiguos."
                ],
                "reglas_json_faltantes": [
                "Estructura obligatoria: { 'treatmentMissing': { 'cedula': '', 'nombreTratamiento': '', 'especialidad': '', 'fechaInicio': '', 'fechaFin': '', 'nombreMedicamento': '', 'dosis': '', 'concentracion': '', 'presentacion': '', 'frecuencia': '', 'reminder': { 'minutosFaltantes': '', 'notas': '', 'estadoEnvio': '', 'estadoRespuesta': '', 'fechaEnvio': '', 'fechaRespuesta': '' } } }",
                "Solo incluir los campos que **NO** se encontraron en el JSON principal (receta).",
                "Los campos faltantes deben quedar como cadena vacía (\"\").",
                "Si la especialidad falta, usar el valor por defecto: 'No aplica'."
                ],
                "condicion_minima_informacion": "Si el texto OCR contiene menos del 50% de la información requerida, devolver la siguiente estructura en lugar de los dos JSON: { 'status': 'insufficient_data', 'message': 'El texto OCR es demasiado escaso para un análisis completo.' }",
                "entrada_ocr": "El texto OCR detectado se proporcionará después de estas instrucciones."
            },
            {
                textoOCR: ${imageText.text}
            }
        `

            const result = await this.ai.models.generateContent({
                model: "gemini-2.5-flash",
                contents: prompt,
            });
            const text: string = result.candidates[0].content.parts[0].text;
            const dataJson = JSON.parse(text.replace(/```json/gi, '').replace(/```/g, '').trim());
            return dataJson;
        }

}
