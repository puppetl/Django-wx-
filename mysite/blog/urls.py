#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2020/2/9 13:10:59
# @License :   (C) Copyright 2020, {python_1904}


# 应用路由
from django.urls import path, include
import blog.views



urlpatterns = [
    path('hello', blog.views.index),
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page),
    # path('detail', blog.views.get_detail_page),
    path('detail/<int:article_id>', blog.views.get_detail_page),
    path('404', blog.views.not_find_page),
    path('edit', blog.views.edit_page),
    path('edit/0', blog.views.edit),
    path('image', blog.views.image),
    path('image1', blog.views.ImageView.as_view()),  # 视图类
    path('imagetext', blog.views.ImageText.as_view()), # 视图类
    path('cookietest', blog.views.CookieTest.as_view()),# 视图类
    path('cookieaccept', blog.views.CookieAccept.as_view()),# 视图类
    path('authorize', blog.views.Authorize.as_view()),# 视图类
    path('logout', blog.views.Logout.as_view())# 视图类


]

