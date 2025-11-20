import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ValidationPipe } from '@nestjs/common';
import { join } from 'path';
import * as express from 'express';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.useGlobalPipes(
    new ValidationPipe({
      forbidNonWhitelisted: true,
      whitelist: true,
      transformOptions: {enableImplicitConversion: true}
    })
  )


  //Configuracion para contenido estatico
  app.use('/files/photo', express.static(join(__dirname, './static/images')));

  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
