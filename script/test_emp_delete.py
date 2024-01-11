import logging
import unittest

from api.ihrm_emp import IhrmEmpApi
from commons.get_header import get_header


class TestEmpDelete(unittest.TestCase):
    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = IhrmEmpApi()
        cls.header = get_header()

    def test_delete_emp(self):
        # 测试数据
        emp_id = "1594551434005712896"
        # 发送请求
        response = self.emp_api.delete_emp(emp_id, self.header)
        json_data = response.json()
        logging.info(f"删除员工的结果为：{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, json_data.get("success"))
        self.assertEqual(10000, json_data.get("code"))
        self.assertEqual("操作成功!", json_data.get("message"))
