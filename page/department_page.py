# -*- coding: utf-8
# create_time: 2021-02-24
from config.config import LOGGER
from page.base_page import BasePage


class DepartmentPage(BasePage):
    """部门管理page类"""
    def add_department(self,add_department:dict):
        """
        添加部门接口封装
        :param add_department: 添加部门请求参数
        :return: 接口响应对象
        """
        try:
            # 生成请求数据
            json_data = add_department
            # 发送请求
            r = self.session.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",json=json_data)
            LOGGER.info('Access to "add_department" url https://qyapi.weixin.qq.com/cgi-bin/department/create success')
            return r
        except Exception as e:
            LOGGER.error('Access to "add_department" url https://qyapi.weixin.qq.com/cgi-bin/department/create failed')
            raise e

    def del_department(self,del_deparment:dict):
        """
        删除部门接口封装
        :param del_deparment: 删除部门请求参数
        :return: 接口响应对象
        """
        try:
            # 生成请求数据
            json_data = del_deparment
            # 发送请求
            id = del_deparment.get('id')
            r = self.session.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?id={id}")
            LOGGER.info(f'Access to "del_department" url https://qyapi.weixin.qq.com/cgi-bin/department/delete?id={id} success')
            return r
        except Exception as e:
            LOGGER.error(
                f'Access to "del_department" url https://qyapi.weixin.qq.com/cgi-bin/department/delete?id={id} failed')
            raise e


