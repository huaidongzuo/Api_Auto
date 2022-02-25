# -*- coding: utf-8 -*-
# 封装日志处理文件
# author:hzuo

import logging
import os.path

class Logger:

    def __init__(self,logger_name,log_dirname='log',log_name='api.log'):
        self.logger = logging.getLogger(log_name) #设置日志的名称
        self.logger.setLevel(logging.DEBUG)

        log_name = log_dirname + '/' + log_name
        print(log_name)

        try:
            fh = logging.FileHandler(log_name,encoding='utf-8')
        except FileNotFoundError:
            os.mkdir(log_name)
            fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        #设置日志格式的输出
        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #添加两个日志实例
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


if __name__ == '__main__':
    Logger("api").logger.debug("测试日志体系构建")
