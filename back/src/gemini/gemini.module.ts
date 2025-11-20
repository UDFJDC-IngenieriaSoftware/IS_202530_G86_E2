import { Module } from '@nestjs/common';
import { GeminiService } from './gemini.service';
import { OcrModule } from 'src/ocr/ocr.module';

@Module({
  providers: [GeminiService],
  exports: [GeminiService],
  imports: [OcrModule]
})
export class GeminiModule {}
