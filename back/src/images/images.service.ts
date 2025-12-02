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
}
