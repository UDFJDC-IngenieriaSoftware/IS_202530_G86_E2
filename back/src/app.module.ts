import { Module } from '@nestjs/common';
import { ImagesModule } from './images/images.module';
import { OcrModule } from './ocr/ocr.module';
import { ConfigModule } from '@nestjs/config';
import { GeminiModule } from './gemini/gemini.module';
import { WhatsappModule } from './whatsapp/whatsapp.module';
import { CommonModule } from './common/common.module';


@Module({
  imports: [
    ConfigModule.forRoot({isGlobal:true}),
    ImagesModule, 
    OcrModule, GeminiModule, WhatsappModule, CommonModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
