from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, FileResponse, JsonResponse
from blog.models import Article, User
from django.core.paginator import Paginator  # 分页组件
from blog import models
import os
from django.conf import settings
# from mysite import settings
from django.views import View  # 类视图
from utils import responseutil
import yaml
from utils.responseutil import ResponseMixin
from utils.responseutil import UtilMixin
import json
import requests

def index(request):  # request接受请求
    return HttpResponse('Hello, World!')


# 实现博客数据返回页面
def article_content(request):
    article = Article.objects.all()[3]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = f'title: {title}, brief_content: {brief_content}, content: {content}, article_id: {article_id}, publish_date: {publish_date}'
    return HttpResponse(return_str)


def get_index_page(request):
    page = request.GET.get('page')  # 获取page参数

    # 将得到字符串page转换为int
    if page:
        page = int(page)
    else:
        page = 1  # 如果没有这个参数,默认为1

    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[:5]  # 已发布日期为准倒序取前5   -号表示倒序
    paginator = Paginator(all_article, 7)  # 定义分页 每页七篇
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)  # 获取page页的内容
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request, 'blog/index.html',
                  {
                      'article_list': page_article_list,  # 当前分页文章
                      'page_num': range(1, page_num + 1),  # 分页数量
                      'curr_page': page,  # 当前页
                      'next_page': next_page,  # 下一页
                      'previous_page': previous_page,  # 上一页
                      'top5_article_list': top5_article_list  # 最近5篇文章
                  }
                  )


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1

        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article
                  }
                  )


def not_find_page(request, exception):
    return render(request, 'blog/404.html')


def show_images(request, article):
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/show_image.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit.html', {'article': article})


def edit(request):
    title = request.POST.get('title', 'TITLE')
    brief_content = request.POST.get('brief_content', 'BRIEF_CONTENT')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, brief_content=brief_content, content=content)
        article = Article.objects.all()

        return render(request, 'blog/index.html', {'article': article})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.brief_content = brief_content
    article.content = content
    article.save()
    return render(request, 'blog/edit.html', {'article': article})


def image(request):
    # from django.conf import settings
    # from mysite import settings
    if request.method == 'GET':
        filename = r'QQ图片20200211132715.jpg'
        filepath = os.path.join(settings.STATIC_ROOT_SELF, filename)
        f = open(filepath, 'rb')
        # with open(filepath, 'rb') as f:
        #     return FileResponse(f, content_type='image/jpg')
        return FileResponse(f, content_type='image/jpg')
    elif request.method == 'POST':
        return HttpResponse('POST QUEST')
    else:
        return HttpResponse(request.method + '没有实现')


class ImageView(View, UtilMixin):
    # from django.views import View  # 类视图
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    # def get(self,request):
    #     filename = r'QQ图片20200211132715.jpg'
    #     filepath = os.path.join(settings.STATIC_ROOT_SELF, filename)
    #     if os.path.exists(filepath):
    #         f = open(filepath, 'rb')
    #         return FileResponse(f, content_type='image/jpg')
    #     else:
    #         return JsonResponse(data={'code':4040,'des':'没有找到图片'})
    def get(self, request):
        filename = r'a843.jpg'
        filepath = os.path.join(settings.STATIC_ROOT_SELF, filename)
        f = open(filepath, 'rb')
        # with open(filepath, 'rb') as f:
        #     return HttpResponse(content=f.read(), content_type='image/jpg')
        # return FileResponse(f, content_type='image/jpg')

        return render(request, 'blog/upfile.html')

    def post(self, request):
        files1 = request.FILES
        # class 'django.utils.datastructures.MultiValueDict'
        # print(type(files))
        picdir = settings.UPLOAD_PIC_DIR

        for key, value in files1.items():
            filename = os.path.join(picdir, key[-8:])
            UtilMixin.savepic(filename, value.read())

        # return HttpResponse(filename)
        return JsonResponse(UtilMixin.wrapdic({'filename': key[-8:]}))

    def delete(self, request):
        picname = request.GET.get('name')
        picdir = settings.UPLOAD_PIC_DIR
        pic_full_path = os.path.join(picdir, picname)
        print('---------->', pic_full_path)
        if not os.path.exists(pic_full_path):
            return HttpResponse('图片不存在')
        else:
            os.remove(pic_full_path)
            return HttpResponse('删除成功')


# class ImageText(View):
class ImageText(View, ResponseMixin):
    # def get(self, request):
    #     return JsonResponse({'code': 1000, 'des': '请求成功'})
    # def get(self, request):
    # return JsonResponse(data={'url': 'xxxxx', 'des': 'fun', 'code': 1000, 'codesdes': 'ok'})
    # return JsonResponse(data=self.wrapjson({'url': 'xxxxx', 'des': 'fun'}))
    # return JsonResponse(data= responseutil.wrap_response({'url': 'xxxxx', 'des': 'fun'}))
    # return JsonResponse(data=self.wrap_response({'url': 'xxxxx', 'des': 'fun', 'code':3003}))

    def get(self, request):
        return render(request, 'blog/imagetext.html', {'des': '图片描述', 'url': '/blog/image'})

    # 提取公共状态信息
    def wrapjson(self, response):
        response['code'] = 1000
        response['codesdes'] = '没有发现问题'
        return response


class CookieTest(View):

    def get(self, request):
        # print(dir(request))
        request.session['mykey'] = '我的值'
        return JsonResponse({'key': 'value'})


class CookieAccept(View):

    def get(self, request):
        # print(dir(request))
        print(request.session['mykey'])
        print(request.session.items())
        return JsonResponse({'key2': 'value2'})


class Authorize(View):
    def get(self, request):
        return HttpResponse('此接口不支持get')
    def post(self, request):
        print(request.body)
        bodystr = request.body.decode('utf8')
        print('bodystr---->', bodystr)
        bodydict = json.loads(bodystr)
        print('bodydict---->', bodydict)
        js_code = bodydict.get('code')
        print('code------->', js_code)
        nickname = bodydict.get('nickname')
        print('nickname------->', nickname)
        appid = settings.APPID
        secret = settings.APPSECRET
        url = f'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={js_code}&grant_type=authorization_code'
        res = requests.get(url)
        print(res.text)  # {"session_key":"dVs1OcA9mGX+kUdnMRGQFQ==","openid":"omhrO4pE67Nrg2gfPkMGXZjh0v7M"}
        res_dict = json.loads(res.text)
        openid = res_dict.get('openid')
        if not openid:
            return HttpResponse('Authorize fail')
        request.session['openid'] = openid
        request.session['id_authorized'] = True
        if not User.objects.filter(openid=openid):
            newuser = User(openid=openid, nickname=nickname)
            newuser.save()
        return HttpResponse('Authorize post ok!')
class Logout(View):
    def get(self, request):
        request.session.clear()
        return JsonResponse(data={'key':'logout'}, safe=False)
class Status(View):
    def get(self, request):
        pass