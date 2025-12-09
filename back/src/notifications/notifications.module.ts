import { Module } from '@nestjs/common';
import { NotificationsService } from './notifications.service';
import { NotificationsController } from './notifications.controller';
import { ConfigModule } from '@nestjs/config';
import { CommonModule } from 'src/common/common.module';
import { WhatsappModule } from 'src/whatsapp/whatsapp.module';

@Module({
  controllers: [NotificationsController],
  providers: [NotificationsService],
  imports: [
    ConfigModule,
    CommonModule,
    WhatsappModule
  ]
})
export class NotificationsModule {}
