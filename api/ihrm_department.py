# 导包
import requests

# 封装测试类
import config


class DepartmentApi(object):
    # 定义初始方法
    def __init__(self):
        self.department_url = config.URL + "/api/company/department"

    # 定义测试接口方法
    # 组织架构列表接口
    def department(self, header):
        return requests.get(self.department_url, headers=header)

    # 获取部门信息接口
    def get_department_information(self, header, dep_id):
        information_url = self.department_url + dep_id
        return requests.get(information_url, headers=header)

    # 部门添加接口
    def department_add(self, header, json_data):
        return requests.post(self.department_url, headers=header, json=json_data)

    # 部门修改接口
    def department_modify(self, header, dep_id, json_data):
        dep_modify_url = self.department_url + dep_id
        return requests.put(dep_modify_url, headers=header, json=json_data)

    # 删除部门接口
    def department_delete(self, header, dep_id):
        dep_delete_url = self.department_url + dep_id
        return requests.delete(dep_delete_url, headers=header)
