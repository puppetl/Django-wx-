from django.test import TestCase
# Create your tests here.
import yaml
filepath = r'F:\django_project\mysite\mysite\myappconfig.yaml'
with open(filepath, 'r', encoding='utf8') as f:
    res = yaml.load(f, Loader=yaml.FullLoader)
    print(res)
