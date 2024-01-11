# 1、导包
import requests

# 2、封装测试类
import config


class LoginApi(object):
    # 定义初始化方法
    def __init__(self):
        self.login_url = config.URL + "/api/sys/login"

    # 定义测试接口方法
    # 登录方法
    def login(self, json_data):
        header = {"Content-Type": "application/json"}
        return requests.post(self.login_url, headers=header, json=json_data)
