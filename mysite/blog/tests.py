from django.test import TestCase
import django
import os
import random

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()


# Create your tests here.
def ranstr(length):
    CHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(length):
        salt += random.choice(CHS)
    return salt


from blog.models import User
from django.db.models import Q  #  使用 Q 对象构建复杂的查询语句
# 查询
res1 = User.objects.filter(nickname__contains='张')  # 模糊查询
# res = User.objects.get(nickname='1')  # 精确查询
users = User.objects.filter(open_id__contains='test_').order_by('open_id')  # 连锁查询
res2 = User.objects.get(Q(openid='test_openid') | Q(nickname='test_nickname'))
res3 = User.objects.filter(Q(openid='test_openid') & Q(nickname='test_nickname'))

print(res1)
print(users)


# 增加
def add_one():
    user = User(openid='test_openid', nickname='test_nickname')  # 第一种
    # User.objects.create(openid='test_openid2', nickname='test_nickname2')  # 第二种
    user.save()


# add_one()

# 批量添加
def add_batch():
    new_user_list = []
    for i in range(10):
        open_id = ranstr(32)
        nickname = ranstr(10)
        user = User(open_id=open_id, nickname=nickname)
        new_user_list.append(user)
    User.objects.bulk_create(new_user_list)


# add_batch()


# 修改一个
def modify_one():
    user = User.objects.get(open_id='test_open_id')
    user.nickname = 'modify_username'
    user.save()


# modify_one()

# 批量改
def modify_batch():
    User.objects.filter(open_id__contains='test_').update(nickname='modify_uname')


# 删一个
def delete_one():
    User.objects.get(open_id='test_open_id').delete()


# 批量删除
def delete_batch():
    User.objects.filter(open_id__contains='test_').delete()


# 全部删除
def delete_all():
    User.objects.all().delete()
    # User.objects.delete()


# ---------数据库函数----------------
# 数据库函数
# 字符串拼接：Concat

from django.db.models import Value
from django.db.models.functions import Concat


# annotate创建对象的一个属性, Value,如果不是对象中原有属性
def concat_function():
    user = User.objects.filter(open_id='test_open_id').annotate(
        # open_id=(open_id), nickname=(nickname)
        screen_name=Concat(
            Value('open_id='),
            'open_id',
            Value(', '),
            Value('nickname='),
            'nickname')
    )[0]
    print('screen_name = ', user.screen_name)


# 字符串长度： Length
from django.db.models.functions import Length


def length_function():
    user = User.objects.filter(open_id='test_open_id').annotate(
        open_id_length=Length('open_id'))[0]

    print(user.open_id_length)


# 大小写函数
from django.db.models.functions import Upper, Lower


def case_function():
    user = User.objects.filter(open_id='test_open_id').annotate(
        upper_open_id=Upper('open_id'),
        lower_open_id=Lower('open_id')
    )[0]
    print('upper_open_id:', user.upper_open_id, ', lower_open_id:', user.lower_open_id)
    pass


# 日期处理函数
# Now()

from blog.models import Article
from django.db.models.functions import Now
from datetime import datetime

dt = datetime(day=1,year=2020,month=3)
# print(dt)

def now_function():
    # 当前日期之前发布的所有应用
    apps = Article.objects.filter(publish_date__lte=Now())
    for app in apps:
        print(app)


# 时间截断函数
# Trunc
from django.db.models import Count
from django.db.models.functions import Trunc


def trunc_function():
    # 打印每一天发布的应用数量
    article_per_day = Article.objects.annotate(publish_day=Trunc('publish_date', 'month')) \
        .values('publish_day') \
        .annotate(publish_num=Count('article_id'))

    for article in article_per_day:
        print('date:', article['publish_day'], ', publish num:', article['publish_num'])


