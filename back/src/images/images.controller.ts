import { Controller, Get, Param, Post, Res, UploadedFile, UseInterceptors } from '@nestjs/common';
import { ImagesService } from './images.service';
import { FileInterceptor } from '@nestjs/platform-express';
import { diskStorage } from 'multer';
import { FileNamer } from './helpers/fileNamer.helper';
import { FileFilter } from './helpers/fileFilter.helper';
import  { Response } from 'express';

@Controller('images')
export class ImagesController {
  constructor(private readonly imagesService: ImagesService) {}


  @Post('sendPhoto')
  @UseInterceptors(FileInterceptor('file',{
    fileFilter: FileFilter,
    storage: diskStorage({
      destination: './static/images',
      filename: FileNamer
    })
  }))
  postPhoto(
    @UploadedFile() file: Express.Multer.File
  ){
    return this.imagesService.getJson(file.filename)
  }
  
  // @Get('getImage/:imageId')
  // getImage(
  //   @Res() res: Response,
  //   @Param('imageId') imageId: string
  // ){
  //   const path = this.imagesService.getImage(imageId);
  //   res.sendFile(path);
  //   return path
  // }

  

}