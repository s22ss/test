# 导包
import logging
import unittest
from parameterized import parameterized

import config
from api.ihrm_emp import IhrmEmpApi
from commons.assert_util import assert_util
from commons.get_header import get_header
from commons.read_json_util import read_json_data


# 定义测试类
class TestEmpQuery(unittest.TestCase):
    # 类属性
    header = None
    # 数据文件的路径
    path_filename = config.BASE_DIR + "/data/query_emp.json"

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = IhrmEmpApi()
        cls.header = get_header()

    # 调用查询员工的接口测试方法
    @parameterized.expand(read_json_data(path_filename))
    def test01_query_emp(self, emp_id, status_code, success, code, message):
        # 发送请求
        response = self.emp_api.query_emp(emp_id, self.header)
        json_data = response.json()
        logging.info(f"查询员工的结果为：{json_data}")

        # 结果断言
        assert_util(self, response, json_data, status_code, success, code, message)
