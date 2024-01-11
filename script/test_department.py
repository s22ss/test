# 1、导包
import logging
import unittest

from parameterized import parameterized

import config
from api.ihrm_department import DepartmentApi
from commons.assert_util import assert_util
from commons.get_header import get_header
# 2、定义测试类
from commons.read_json_util import read_json_data


class TestDepartment(unittest.TestCase):
    # 类属性
    header = None
    # 数据文件的路径
    information_path_filename = config.BASE_DIR + "/data/department_information.json"
    department_add_path_filename = config.BASE_DIR + "/data/department_add.json"
    department_modify_path_filename = config.BASE_DIR + "/data/department_modify.json"
    department_delete_path_filename = config.BASE_DIR + "/data/department_delete.json"

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.department_api = DepartmentApi()
        cls.header = get_header()

    # 调用已封装的测试接口的方法
    # 调用组织架构列表接口的方法
    def test01_department(self):
        response = self.department_api.department(self.header)
        json_data = response.json()
        logging.info(f"组织结构列表的结果为：{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, json_data.get("success"))
        self.assertEqual(10000, json_data.get("code"))
        self.assertEqual("操作成功！", json_data.get("message"))

    # 调用获取部门信息接口的方法
    @parameterized.expand(read_json_data(information_path_filename))
    def test02_get_department_information(self, dep_id, status_code, success, code, message):
        # 发送请求
        response = self.department_api.get_department_information(self.header, dep_id)
        json_data = response.json()
        logging.info(f"获取部门信息的结果为：{json_data}")
        # 断言结果
        assert_util(self, response, json_data, status_code, success, code, message)

    # 调用添加部门接口的方法
    @parameterized.expand(read_json_data(department_add_path_filename))
    def test03_department_add(self, desc, add_data, status_code, success, code, message):
        # 发送请求
        response = self.department_api.department_add(self.header, add_data)
        json_data = response.json()
        logging.info(f"添加部门的结果为：{json_data}")
        # 结果断言
        assert_util(self, response, json_data, status_code, success, code, message)

    # 调用部门修改接口的方法
    @parameterized.expand(read_json_data(department_modify_path_filename))
    def test04_department_modify(self, desc, dep_id, modify_data, status_code, success, code, message):
        # 发送请求
        response = self.department_api.department_modify(self.header, dep_id, modify_data)
        json_data = response.json()
        logging.info(f"部门修改的结果为：{json_data}")
        # 结果断言
        assert_util(self, response, json_data, status_code, success, code, message)

    # 调用删除部门接口的方法
    @parameterized.expand(read_json_data(department_delete_path_filename))
    def test05_department_detele(self, dep_id, status_code, success, code, message):
        # 发送请求
        response = self.department_api.department_delete(self.header, dep_id)
        json_data = response.json()
        logging.info(f"删除部门的结果为：{json_data}")
        # 结果断言
        assert_util(self, response, json_data, status_code, success, code, message)
