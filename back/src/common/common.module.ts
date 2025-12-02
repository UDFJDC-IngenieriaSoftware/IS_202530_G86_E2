import { Module } from '@nestjs/common';
import { CommonService } from './common.service';
import { CommonController } from './common.controller';
import { AxiosAdapter } from './adapters/axios.adapter';

@Module({
  controllers: [CommonController],
  providers: [CommonService, AxiosAdapter],
  exports: [
    AxiosAdapter
  ]
})
export class CommonModule {}
