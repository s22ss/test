# -*- coding: utf-8 -*-

import logging
import os

from tools.url import get_base_dir

# 目录配置

# 项目目录
BASEDIR = get_base_dir()
# 临时图片目录
IMAGESDIR = os.path.join(BASEDIR, "images")
# 测试数据目录
TESTDATA = os.path.join(BASEDIR, "data/contact_data")

# 日志配置

import os
from tools.log import GetLog
from tools.strtime import get_now_time

LOG_NAME = 'ROOT'
LOG_PATH = os.path.join(BASEDIR, f'logs/{get_now_time()}.log')
LOG_LEVEL = logging.INFO
LOG_FORMAT = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d-%(funcName)s')

# 实例化以后Logger对象
LOGGER = GetLog().get_logger(name=LOG_NAME, level=LOG_LEVEL, fromt=LOG_FORMAT, path=LOG_PATH)
