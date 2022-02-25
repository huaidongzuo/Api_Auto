# -*- coding: utf-8 -*-
# 封装接口数据
# author:hzuo

from system.Log import Logger
log = Logger('api_test')

def api(protocol,host,port,method,path=None,**kwargs):
    kwargs.update(
        {
            'url' : f"{protocol}://{host}:{port}/{path}",
            'method' : method
        }
    )
    for key in kwargs:
        log.logger.info(f"api中有：{key},值为:{kwargs[f'{key}']}")

    return kwargs