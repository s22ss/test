# 1、导包
import logging
import unittest

from commons.assert_util import assert_util
from commons.read_json_util import read_json_data
from parameterized import parameterized

import config
from api.login import LoginApi


# 2、定义测试类
class TestLoginApi(unittest.TestCase):
    # 类属性
    header = None

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    path_filename = config.BASE_DIR + "/data/ihrm_login.json"

    # 调用已封装的测试接口的方法
    # #调用登录接口方法
    @parameterized.expand(read_json_data(path_filename))
    def test01_login(self, desc, req_body, status_code, success, code, message):
        # 发送请求
        resp = self.login_api.login(req_body)
        json_data = resp.json()
        logging.info(f"登录的结果为：{json_data}")

        # 结果断言
        assert_util(self, resp, json_data, status_code, success, code, message)
