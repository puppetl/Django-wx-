from django.contrib import admin

# Register your models here.

from .models import Article
# from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')   # 后台显示标题,日期
    list_filter = ('publish_date',)   # 过滤器


admin.site.register(Article, ArticleAdmin)  # 将模型注册到admin中
# admin.site.register(Article)  # 将模型注册到admin中

