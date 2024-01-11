import unittest

from parameterized import parameterized

from commons.read_json_util import read_json_data

base_url = 'https://api.52vmy.cn/api/query/daxue'

path_filename = 'C:\\Users\\黎枝斌\\Desktop\\apiTestIhrm-master\\data\\school.json'


class Api(unittest.TestCase):
    # 类属性
    header = None

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.requests = None

    @parameterized.expand(read_json_data(path_filename))
    def school(self, name, code, msg):
        params = {'daxue': name}
        response = self.requests.get(base_url, params=params)
        print(response.text)
        data = response.json()

        # 对返回的数据进行断言
        assert data['code'] == code
        assert data['msg'] == msg
        print("断言成功")


if __name__ == '__main__':
    ret = Api()
    print(ret)
