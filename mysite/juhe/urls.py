#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2020/2/17 14:33:32
# @License :   (C) Copyright 2020, {python_1904}

from django.urls import path

import juhe.views


urlpatterns = [
    path('joke/', juhe.views.joke),
    path('image/', juhe.views.image),
    path('test/', juhe.views.testrequest),
    path('apps/', juhe.views.apps),

]



