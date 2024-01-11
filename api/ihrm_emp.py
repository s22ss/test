# 1、导包
import requests

import config


# 2、封装测试类
class IhrmEmpApi(object):
    # 定义初始化方法
    def __init__(self):
        self.emp_url = config.URL + "/api/sys/user/"

    # 定义测试接口方法
    # 添加员工接口
    def add_emp(self, header, json_data):
        return requests.post(self.emp_url, headers=header, json=json_data)

    # 查询员工接口
    def query_emp(self, emp_id, header):
        new_query_url = self.emp_url + emp_id
        return requests.get(new_query_url, headers=header)

    # 修改员工接口
    def modify_emp(self, emp_id, header, json_data):
        new_modify_url = self.emp_url + emp_id
        return requests.put(new_modify_url, headers=header, json=json_data)

    # 删除员工接口
    def delete_emp(self, emp_id, header):
        new_delete_emp = self.emp_url + emp_id
        return requests.delete(new_delete_emp, headers=header)
