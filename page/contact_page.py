# -*- coding: utf-8 -*-
# createtime: 2021-02-01

from config.config import LOGGER
from page.base_page import BasePage


class ContactPage(BasePage):
    """
    通讯录管理相关接口封装
    """

    def add_remenber(self, add_remenber: dict = None):
        """
        添加成员接口封装
        :param add_remenber: 添加成员接口请求数据
        :return: 接口返回对象
        """
        try:
            # 获取请求数据
            json_data = add_remenber
            # 发送请求
            r = self.session.post(url='https://qyapi.weixin.qq.com/cgi-bin/user/create', json=json_data)
            LOGGER.info('Access to "add_remenber" url https://qyapi.weixin.qq.com/cgi-bin/user/create success')
            return r
        except Exception as e:
            LOGGER.error('Access to "add_remenber" url https://qyapi.weixin.qq.com/cgi-bin/user/create failed')
            raise e

    def find_remenber(self, userid):
        """
        查询成员接口封装
        :param userid: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        :return: 接口返回对象
        """
        try:
            params = {
                "userid": userid
            }
            r = self.session.get(url='https://qyapi.weixin.qq.com/cgi-bin/user/get', params=params)
            LOGGER.info('Access to "find_remenber" url https://qyapi.weixin.qq.com/cgi-bin/user/get success')
            return r
        except Exception as e:
            LOGGER.error('Access to "find_remenber" url https://qyapi.weixin.qq.com/cgi-bin/user/get failed')
            raise e

    def delete_remenber(self, delete_remenber_data: dict):
        """
        删除成员接口封装
        :param delete_remenber_data: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        :return: 接口返回对象
        """
        try:
            params = delete_remenber_data
            r = self.session.get(url='https://qyapi.weixin.qq.com/cgi-bin/user/delete', params=params)
            LOGGER.info('Access to "delete_remenber" url https://qyapi.weixin.qq.com/cgi-bin/user/delete success')
            return r
        except Exception as e:
            LOGGER.error('Access to "delete_remenber" url https://qyapi.weixin.qq.com/cgi-bin/user/delete failed')
            raise e
