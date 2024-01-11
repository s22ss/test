# -*- coding: utf-8 -*-

import logging


class GetLog:
    """
    自定义logging类
    方法：1.get_logger：获取一个Logger对象。
    """

    def get_logger(self, name, level, fromt, path):
        """
        获取Logger对象。
        :param name: Logger名字。
        :param level: Logger级别。
        :param fromt: Logger日志输出级别。
        :param path: 日志文件路径。
        :return: Logger对象
        """
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.hasHandlers():
            # 给Logger添加一个FileHandler
            file_handler = logging.FileHandler(filename=path, encoding='utf-8')
            file_handler.setLevel(level=level)
            file_handler.setFormatter(fmt=fromt)
            self.logger.addHandler(file_handler)
            # 给Logger添加一个FileHandler
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(level=level)
            stream_handler.setFormatter(fmt=fromt)
            self.logger.addHandler(stream_handler)
        return self.logger
