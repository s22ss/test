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


# 2、定义测试类
class TestEmpModify(unittest.TestCase):
    # 类属性
    header = None

    path_filename = config.BASE_DIR + "/data/modify_emp.json"

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = IhrmEmpApi()
        cls.header = get_header()

    # 调用修改员工接口发方法
    @parameterized.expand(read_json_data(path_filename))
    def test_modify_emp(self, emp_id, modify_data, status_code, success, code, message):
        # 发送请求
        response = self.emp_api.modify_emp(emp_id, self.header, modify_data)
        json_data = response.json()
        logging.info(f"修改员工的结果为：{json_data}")
        # 结果断言
        assert_util(self, response, json_data, status_code, success, code, message)
