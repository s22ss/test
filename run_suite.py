# 1、导包
import time
import unittest
from unittestreport import TestRunner

import config
from script.test_department import TestDepartment
from script.test_emp_add import TestEmpAdd
from script.test_emp_modify import TestEmpModify
from script.test_emp_query import TestEmpQuery
from script.test_login import TestLoginApi

# 2、创建测试套件
suite = unittest.TestSuite()

# 3、添加测试用例
suite.addTest(unittest.makeSuite(TestLoginApi))
suite.addTest(unittest.makeSuite(TestEmpAdd))
suite.addTest(unittest.makeSuite(TestEmpQuery))
suite.addTest(unittest.makeSuite(TestEmpModify))
suite.addTest(unittest.makeSuite(TestDepartment))
# 4、执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(suite)


# 5、生成测试报告
# 5.1 定义测试报告文件
rep_file = config.BASE_DIR + "/report/ihrm.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 5.2 创建第三方执行器对象
runner = TestRunner(suite, filename=rep_file, title="ihrm接口测试报告", tester="张三", desc="v1.0", templates=1)
# 5.3 执行器调用run方法执行生成报告
runner.run()
