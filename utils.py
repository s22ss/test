# 1、导包
import logging
from logging import handlers

import config


# 2、定义初始化日志函数
def init_log():
    # 定义定时器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 设置日志的级别

    # 定义处理器
    sh = logging.StreamHandler()  # 控制台处理器
    log_file = config.BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=7,
                                                   encoding="UTF-8")  # 文件处理器

    # 定义格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 设置处理器格式
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
