import { Module } from '@nestjs/common';
import { ImagesModule } from './images/images.module';
import { OcrModule } from './ocr/ocr.module';
import { ConfigModule } from '@nestjs/config';
import { GeminiModule } from './gemini/gemini.module';
import { WhatsappModule } from './whatsapp/whatsapp.module';
import { CommonModule } from './common/common.module';
import { NotificationsModule } from './notifications/notifications.module';
import { ScheduleModule } from '@nestjs/schedule';


@Module({
  imports: [
    ConfigModule.forRoot({isGlobal:true}),
    ScheduleModule.forRoot(),
    ImagesModule, 
    OcrModule, GeminiModule, WhatsappModule, CommonModule, NotificationsModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}
