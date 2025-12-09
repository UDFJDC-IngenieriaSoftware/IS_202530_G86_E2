import { Body, Controller, Get, Post, Query } from '@nestjs/common';
import { WhatsappService } from './whatsapp.service';
import { ConfigService } from '@nestjs/config';

@Controller('whatsapp')
export class WhatsappController {
  constructor(
    private readonly whatsappService: WhatsappService,
    private readonly configService: ConfigService
  ) {}

  @Get()
  verifyWebhook(
  @Query('hub.mode') mode: string,
  @Query('hub.verify_token') token: string,
  @Query('hub.challenge') challenge: string,
  ) {
    console.log('Intentando verificar webhook...', { mode, token, challenge });

    if (mode === 'subscribe' && token === this.configService.get('NGROK_KEY')) {
      console.log('Webhook verificado correctamente');
      return challenge; // Meta necesita que devolvamos esto
    }

    console.log('Error de verificación: token inválido');
    return 'Error: token inválido';
  }

  // POST: recepción de mensajes
  @Post()
  receiveMessage(@Body() body: any) {
    console.log("funciona");
    this.whatsappService.handleIncomingMessage(body);
    return { status: 'received' };
  }
  
}
