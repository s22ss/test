# 1、导包
import logging
import unittest

from parameterized import parameterized

import config
from api.ihrm_emp import IhrmEmpApi
from commons.assert_util import assert_util
from commons.db_util import DBUtil
from commons.get_header import get_header
from commons.read_json_util import read_json_data
from config import TEL


# 2、定义测试类
class TestEmpAdd(unittest.TestCase):
    # 类属性
    header = None

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = IhrmEmpApi()
        cls.header = get_header()
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.uid_db(delete_sql)

    def tearDown(self) -> None:
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.uid_db(delete_sql)

    path_filename = config.BASE_DIR + "/data/add_emp.json"

    # 调用添加员工接口方法
    @parameterized.expand(read_json_data(path_filename))
    def test01_add_emp(self, desc, add_data, stauts_code, success, code, message):
        # 发送请求
        response = self.emp_api.add_emp(self.header, add_data)
        json_data = response.json()
        logging.info(f"添加员工结果为：{json_data}")
        # 结果断言
        assert_util(self, response, json_data, stauts_code, success, code, message)
