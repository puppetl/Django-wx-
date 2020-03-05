[toc]







MTV:Model:模型

Django ORM

![1582973310505](C:\Users\86151\AppData\Roaming\Typora\typora-user-images\1582973310505.png)







## 跨DB迁移

- why : 从sqlite到mysql

  - sqlite3在项目初期便利
  - sqlite3是文件数据库,性能跟不上
  - mysql是工业界常用的数据库(免费开源)

- Django ORM 框架

  - ![1583064338731](C:\Users\86151\AppData\Roaming\Typora\typora-user-images\1583064338731.png)
  - 屏蔽了数据库差异
  - 提供了迁移工具
  - 简化了开发流程

- 迁移过程

  - 重要的东西

    - 数据
    - 表结构

  - 数据备份

    - python manage.py  dumpdata 应用名 >xx.json
  - 如果想备份所有应用数据python manage.py  dumpdata  >xx.json
  
- 表结构同步
  
  - 创建MySQL数据库并更新配置
  
    - 创建好mysql数据库的库,表
  
    -  https://docs.djangoproject.com/en/3.0/ref/settings/#databases 
  
      - ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'mydatabase',
                'USER': 'mydatabaseuser',
                'PASSWORD': 'mypassword',
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
        }
      ```
  
  - 创建slave数据库
  
      - ![1583065363242](C:\Users\86151\AppData\Roaming\Typora\typora-user-images\1583065363242.png)
    - 数据和default数据库可以同步
  
  - 迁移数据库表
  
      - python manage.py  migrate --run-syncdb --database slave
      - slave为目标数据库
    - 迁移完成后查看mysql数据表
  
- 数据迁移
  
    - 启用mysql配置
    - python manage.py loaddata xx.json

## 数据库索引

- 索引的概述

  - 例子:书的目录
  - 辅助数据结构,为了快速找到想要的数据
  - ![1583065825066](C:\Users\86151\AppData\Roaming\Typora\typora-user-images\1583065825066.png)
  - B+树
  - 加快检索数据的速度
  - 降低**插入删除更新**的速度

- 应该被索引的字段

  - 需要排序的的字段(order_by)
  - 需要比较操作的字段(>  <   >=   <=)
  - 需要过滤操作的字段(filter , exclude)

- 添加索引的两种方法

  - 属性中定义

    - 对于模型字段添加db_index=True
    - 任何表结构的改变都需要迁移数据库

  - 模型的Meta属性类

    - ![1583066400605](C:\Users\86151\AppData\Roaming\Typora\typora-user-images\1583066400605.png)

    - 联合索引

    - 

    - django meta类

    - https://docs.djangoproject.com/en/dev/ref/models/options/ 

       https://www.jianshu.com/p/774a8f16d624 

       https://blog.csdn.net/bbwangj/article/details/79967858 

  - 默认的索引规则

    - 主键必定是索引
    - 唯一也是索引
- 外键默认是索引
    
 
    

    
    



## 模型层关系映射

- 三种关系映射
  - 一对一
  - 一对多(多对一)
  - 多对多
  - ![1583067693233](C:\Users\86151\AppData\Roaming\Typora\typora-user-images\1583067693233.png)
  - 父子,父母,兄弟
  - 书和作者的关系
- Django表达三种关系映射
  - 一对一 OneToOneField
  - 一对多(多对一): ForeignKey
  - 多对多:ManyToManyField
- 关系映射实战
  - ![1583196592219](C:\Users\86151\AppData\Roaming\Typora\typora-user-images\1583196592219.png)
  - 外键定义在唯一的那个模型中,比如 elderbrother的fatherid
  - 有没有用到关系映射
  - 用到了哪种关系映射

## 增删改查基本操作

## 



xampp全家桶

