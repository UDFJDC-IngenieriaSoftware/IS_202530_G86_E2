import { BadRequestException, Injectable } from '@nestjs/common';
import { existsSync } from 'fs';
import { join } from 'path';
import { GeminiService } from 'src/gemini/gemini.service';

@Injectable()
export class ImagesService {

    constructor(
        private readonly geminiService: GeminiService,
    ){}



    private getImage(imageId: string){

        const path = join(__dirname, '../../static/images', imageId);
        if(!existsSync(path)){
            throw new BadRequestException(`No image found with id: ${imageId}`);
        }
        return path;
    }


    async getJson(imageId: string){
        const path = this.getImage(imageId);
        return await this.geminiService.getJsonFromDataImage(path);
    }


}
