from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
# Create your views here.
import requests
import yaml

def joke(request):
    # url = 'http://v.juhe.cn/joke/content/list.php?sort=1234567899&page=3&pagesize=5&time=1418816972&key=0bc33fd508311bd135a3e2f19f7d0d99'
    url = 'http://v.juhe.cn/joke/content/list.php?sort=desc&page=5&pagesize=&time=1418816972&key=0bc33fd508311bd135a3e2f19f7d0d99'
    # url = 'http://web.juhe.cn:8080/environment/air/cityair?city=%E5%8C%97%E4%BA%AC&key=c567a7fa7eb18b952aecc0c137ed8acb'
    res = requests.get(url)
    if res.status_code == 200:
        return HttpResponse(res.text)
    else:
        return HttpResponse('没有获取到数据')


def testrequest(request):
    print('请求方法:', request.method)
    print('客户端信息:', request.META)
    print('get请求参数:', request.GET)
    print('请求头:', request.headers)
    print('cookie:', request.COOKIES)
    return JsonResponse({'请求方法': request.method,
                         '客户端信息': 'ssss',
                         '请求头': 'ssss',
                         'cookie': request.COOKIES.__str__()
                         })


def image(request):
    f = open(r'F:\django_project\mysite\static\QQ图片20200211132715.jpg', 'rb')
    # return HttpResponse(content=f.read(), content_type='image/jpg')
    return FileResponse(f, content_type='image/jpg')

def apps(request):
    if request.method == 'POST':
        return HttpResponse('都捏按...')
    filepath = r'F:\django_project\mysite\mysite\myappconfig.yaml'
    with open(filepath, 'r', encoding='utf8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
    # return JsonResponse({'names': ['支付宝', '微信']}, safe=False)   # res.data.names
    # return JsonResponse(['支付宝', '微信'], safe=False)   # res.data
    return JsonResponse(res, safe=False)  # res.data   item.name