# 定义通用的断言方法
def assert_util(self, resp, json_data, status_code, success, code, message):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(success, json_data.get("success"))
    self.assertEqual(code, json_data.get("code"))
    self.assertEqual(message, json_data.get("message"))
