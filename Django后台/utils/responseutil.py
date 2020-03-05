#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2020/2/19 15:29:18
# @License :   (C) Copyright 2020, {python_1904}

def wrap_response(response):
    response['code'] = 1000
    response['codesdes'] = '没有发现问题'
    return response

# Mixin 给类提供某一种能力--->提供某些功能的类
class ResponseMixin():

    @staticmethod
    def wrap_response(response):
        if not response.get('code'):
            response['code'] = Code.SUCCESS
        if not response.get('codesdes'):
            response['codesdes'] = Code.des(response.get('code'))
        return response

class Code:
    SUCCESS = 2000
    FAILED = 2222

    @classmethod
    def des(cls, code):
        if code == cls.SUCCESS:
            return '成功'
        elif code == cls.FAILED:
            return '失败'
        else:
            return 'i also don\'t know'

class UtilMixin():

    @staticmethod
    def savepic(filename, content):
        with open(filename, 'wb') as f:
            f.write(content)

    @staticmethod
    def wrapdic(res_dict):
        """
        返回状态码以及结果,1000 default
        :param res_dict: 需要包裹的返回值字典类型
        :return: 装饰之后的dict
        """
        if not res_dict.get('code'):
            res_dict['code'] = Code.SUCCESS
        if not res_dict.get('codesdes'):
            res_dict['codesdes'] = Code.des(res_dict.get('code'))
        return res_dict