#! /usr/bin/python
# -*- coding: utf-8 -*-
# create_time: 2021-02-26
import os

import pytest
import yaml

from page.contact_page import ContactPage
from config.config import TESTDATA,LOGGER
from page.department_page import DepartmentPage
from page.material_page import MaterialPage


class TestAddRmenber:
    # 获取请求数据
    data_path = os.path.join(TESTDATA, "add_remenber.yaml")
    with open(file=data_path, mode='r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    def setup_class(self):
        self.contact = ContactPage()
        self.department = DepartmentPage(session=self.contact.session)
        self.materia = MaterialPage(session=self.contact.session)


    @pytest.fixture(params=data)
    def get_data(self,request):
        """
        自定义用例的前置后置方法
        :param request:
        :return:
        """
        LOGGER.info('》》》》》》》START TO EXECUTION CASE 》》》》》》')
        LOGGER.info('GENERATE TEST CASE DATA')
        # 生成用例的依赖数据
        add_department_data = request.param.get('add_department')
        up_images_data = request.param.get('up_images')
        re_add_remenber_data = request.param.get('re_add_remenber')
        if add_department_data:                                            # 是否需要临时生成部门
            r = self.department.add_department(add_department_data)
            department_id = r.json()['id']
            assert r.json()['errcode'] == 0

        if up_images_data:                                                 # 是否需要临时上传图片
            r = self.materia.up_image(up_images_data)
            avatar_mediaid = r.json().get('media_id')
            assert r.json()['errcode'] == 0
            request.param['add_remenber']['avatar_mediaid'] = avatar_mediaid

        if re_add_remenber_data:                                            # 是否需要创建两个用户
            r = self.contact.add_remenber(re_add_remenber_data)
            assert r.json()['errcode'] == 0

        yield request.param

        LOGGER.info('CLEAR TEST CASE DATA')

        # 清理用例的依赖数据，及用例数据

        if up_images_data:                                                # 清理图片上传数据
            self.avatar_mediaid = None

        if re_add_remenber_data:                                           # 清理多用户数据
            re_del_remenber_data = {}
            re_del_remenber_data['userid'] = re_add_remenber_data.get('userid')
            r = self.contact.delete_remenber(re_del_remenber_data)
            assert r.json()['errcode'] == 0

        # 清理用例创建的用户
        except_data = request.param.get('expect').get("errcode")
        if except_data == 0:
            del_remenber_data = {}
            del_remenber_data['userid'] = request.param.get('add_remenber').get('userid')
            r = self.contact.delete_remenber(del_remenber_data)
            assert r.json()['errcode'] == 0

        if add_department_data:                                           # 清理department数据
            del_department_data = {}
            del_department_data['id'] = department_id
            r = self.department.del_department(del_department_data)
            assert r.json()['errcode'] == 0
        LOGGER.error("》》》》》》》END TO EXECUTION CASE 》》》》》》")


    # @pytest.mark.parametrize("data",data)
    def test_addremenber(self,get_data):
        """添加成员接口测试用例"""
        LOGGER.info('TEST ADD_REMENBER CASE')
        # 添加成员接口测试
        add_remenber_data = get_data.get('add_remenber')
        r = self.contact.add_remenber(add_remenber_data)
        # 断言
        expect:dict = get_data.get('expect')
        errcode = expect.get('errcode')
        errmsg = expect.get('errmsg')
        if errcode:
            assert r.json()['errcode'] == errcode


if __name__ == "__main__":
    pytest.main(['-vs','test_add_remenber.py'])
