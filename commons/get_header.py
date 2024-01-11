# 1、导包
import requests

import config


# 2、定义函数
def get_header():
    url = config.URL + "/api/sys/login"
    data = {"mobile": "13800000002", "password": "123456"}
    resp = requests.post(url=url, json=data)
    # 从响应体中，获取data的值
    token = resp.json().get("data")
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    return header
