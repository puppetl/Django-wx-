# Django -Mysql数据库利用pymysql数据迁移

Django自带的有数据库sqlite，但是有很多小伙会想用mysql的数据库，但是在sqlite上已经写了部分数据，那一定就涉及到了数据迁移。

### 一、更换默认数据库

需要在Django的项目的setting里，更改默认的数据库。



```csharp
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

这是原先的默认数据库，改为下面的数据库即可。注意的是用户名密码端口等，要跟自己的mysql匹配。先不要删除原先的数据库，等会儿要用到，注释起来。



```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_db',
        'USER': 'root',
        'PASSWORD': 'root123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 二、迁移数据库

在终端输入

1、制作数据库同步文件

```shell
python manage.py makemigrations
```

2、同步模型到数据库

```shell
 python manage.py migrate
```

但是可能会报错。如下图



![img](https://upload-images.jianshu.io/upload_images/16404073-d5968b1d16e9deec.png?imageMogr2/auto-orient/strip|imageView2/2/w/1058/format/webp)

提醒没有安装mysqlclient.png



紧接着，有些人（如本人）去安装这个mysqlclient



![img](https://upload-images.jianshu.io/upload_images/16404073-dd6eff859b559795.png?imageMogr2/auto-orient/strip|imageView2/2/w/1076/format/webp)

安装mysqlclient.png


本以为可以用了，结果还是报错说本人没有安装mysqlclient。还是不能用。本人并不太清楚为什么mysqlclient不能用。

1、安装pymysql



```undefined
pip install pymysql
```

2、打开项目的*init*.py输入



```swift
import pymysql
pymysql.install_as_MySQLdb()
```

3、这时候就可以迁移数据库了。



![img](https://upload-images.jianshu.io/upload_images/16404073-10c4f4d488b18129.png?imageMogr2/auto-orient/strip|imageView2/2/w/1136/format/webp)

成功迁移数据库.png

### 三、迁移数据

这里就需要用到之前的sqlite的数据了，也就是让大家先注释起来的源代码
1、导出数据
把mysql的代码段注释起来，然后选用sqlite的代码段。运行下面代码



```css
python manage.py dumpdata > data.json
```

此刻可以在文件夹里看到多出来的一个data.json的文件，这就是我们需要的数据

 2、导入数据
注释掉sqlite的代码段，选用mysql的代码段。运行下面代码

```css
python manage.py loaddata data.json
```

3、导入成功

### 四、可能遇到的问题

##### 1、缓存表不存在

![img](https://upload-images.jianshu.io/upload_images/16404073-3785ec03eb360b14.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

缓存表不存在.png



建立一个缓存表即可



```css
python manage.py createcachetable
```

##### 2、如果在迁移数据的时候遇见数据重复报错

![img](https://upload-images.jianshu.io/upload_images/16404073-ff0915e6b62a3b29.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

数据重复.png



进入数据库删除两行数据即可



![img](https://upload-images.jianshu.io/upload_images/16404073-949adb689d52d912.png?imageMogr2/auto-orient/strip|imageView2/2/w/930/format/webp)

删除两行代码.png