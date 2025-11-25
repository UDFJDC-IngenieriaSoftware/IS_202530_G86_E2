import { Module } from '@nestjs/common';
import { GeminiService } from './gemini.service';
import { OcrModule } from 'src/ocr/ocr.module';
import { ConfigModule } from '@nestjs/config';

@Module({
  providers: [GeminiService],
  exports: [GeminiService],
  imports: [
    ConfigModule,
    OcrModule]
})
export class GeminiModule {}
