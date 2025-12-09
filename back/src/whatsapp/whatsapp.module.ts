import { Module } from '@nestjs/common';
import { WhatsappService } from './whatsapp.service';
import { WhatsappController } from './whatsapp.controller';
import { CommonModule } from 'src/common/common.module';
import { ConfigModule } from '@nestjs/config';
import { ImagesModule } from 'src/images/images.module';

@Module({
  controllers: [WhatsappController],
  providers: [WhatsappService],
  imports: [
    CommonModule,
    ConfigModule,
    ImagesModule
  ],
  exports:[
    WhatsappService
  ]
})
export class WhatsappModule {}
