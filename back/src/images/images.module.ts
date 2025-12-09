import { Module } from '@nestjs/common';
import { ImagesService } from './images.service';
import { ImagesController } from './images.controller';
import { GeminiModule } from 'src/gemini/gemini.module';
import { OcrModule } from 'src/ocr/ocr.module';
import { CommonModule } from 'src/common/common.module';

@Module({
  controllers: [ImagesController],
  providers: [ImagesService],
  imports: [GeminiModule,
    CommonModule
  ],
  exports: [ImagesService]
})
export class ImagesModule {}
