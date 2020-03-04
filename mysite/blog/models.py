from django.db import models


# Create your models here.
class Article(models.Model):
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章内容
    content = models.TextField()
    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True)  # 如果没有指定日期,默认当前日期为发布日期--->auto_now

    # 后台列表显示为文章的标题
    def __str__(self):
        return self.title


class User(models.Model):
    openid = models.CharField(max_length=64, unique=True)
    nickname = models.CharField(max_length=64)
    # nickname = models.CharField(max_length=64, db_index=True)
    # manufacturer = models.ForeignKey(
        #     'Article',
        #     on_delete=models.CASCADE,
        # )
    # authors = models.ManyToManyField('Article')
    # friends = models.ManyToManyField("self")   # Model也可以与自身做多对多关系
    def __str__(self):
        return self.nickname
    class Meta:
        """
        元: 描绘本身
        """
        # db_table = 'abc'   # 该变表名
        # app_label = 'User'   # 定义模型类属于哪一个应用
        indexes = [
            models.Index(fields=['nickname'], name='nickname'),
        ]