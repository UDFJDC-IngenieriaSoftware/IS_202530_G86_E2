import { Injectable } from "@nestjs/common";
import { createWorker } from "tesseract.js";

@Injectable()
export class OcrService {

    async readImageBuffer(buffer: Buffer): Promise<{ text: string }> {
        const worker = await createWorker("spa", 1);

        try {
            const result = await worker.recognize(buffer);
            return { text: result.data.text };
        } finally {
            await worker.terminate();
        }
    }
} 
