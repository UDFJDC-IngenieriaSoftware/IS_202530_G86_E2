import { Module } from '@nestjs/common';
import { ImagesModule } from './images/images.module';
import { OcrModule } from './ocr/ocr.module';
import { ConfigModule } from '@nestjs/config';
import { GeminiModule } from './gemini/gemini.module';


@Module({
  imports: [
    ConfigModule.forRoot({isGlobal:true}),
    ImagesModule, 
    OcrModule, GeminiModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
