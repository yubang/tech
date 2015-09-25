# coding:UTF-8


from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from tech.models import ArticleModel, ArticleReadNumber
from django.db.models import F
import json


def get_labels(obj):
    """
    获取标签列表
    :param label: 标签字符串
    :return: list
    """
    if obj:
        obj.label = obj.label.split(",")
    return obj


def index(request):

    json_text = """
        [
            {
                "name" : "语言官网",
                "content" : [
                    {"href": "https://www.python.org/", "content": "python"},
                    {"href": "https://golang.org/", "content": "go"},
                    {"href": "http://php.net/", "content": "php"},
                    {"href": "http://www.java.com/zh_CN/", "content": "java"},
                    {"href": "https://www.ruby-lang.org/zh_cn/", "content": "ruby"}
                ]
            },
            {
                "name" : "开发工具",
                "content" : [
                    {"href": "http://www.eclipse.org/downloads/", "content": "eclipse"},
                    {"href": "http://www.jetbrains.com/pycharm/download/", "content": "pycharm"},
                    {"href": "https://github.com/visualfc/liteide", "content": "liteide"},
                    {"href": "http://dbeaver.jkiss.org/", "content": "dbeaver"},
                    {"href": "http://git-cola.github.io/", "content": "cola"}
                ]
            },
            {
                "name" : "开发社区",
                "content" : [
                    {"href": "http://www.oschina.net/", "content": "oschina"},
                    {"href": "http://www.v2ex.com/", "content": "v2ex"},
                    {"href": "http://stackoverflow.com/", "content": "stackoverflow"},
                    {"href": "https://ruby-china.org/", "content": "ruby china"}
                ]
            },
            {
                "name" : "网站相关",
                "content" : [
                    {"href": "http://www.aliyun.com/", "content": "阿里云"},
                    {"href": "http://www.qiniu.com/", "content": "七牛"},
                    {"href": "http://changyan.kuaizhan.com/", "content": "畅言"}
                ]
            },
            {
                "name" : "在线工具",
                "content" : [
                    {"href": "http://tool.oschina.net/", "content": "开源中国"}
                ]
            }
        ]
    """

    navigations = json.loads(json_text)
    return render_to_response("article/index.html", {'navigations': navigations})


def content(request, article_id):
    try:
        obj = ArticleModel.objects.get(id=article_id)
        obj = get_labels(obj)

        t = ArticleReadNumber.objects.get(article_id=obj.id)
        t.read_number = F("read_number") + 1
        t.save()
        
        t = ArticleReadNumber.objects.get(article_id=obj.id)
        obj.read_number = t.read_number

    except ObjectDoesNotExist:
        return HttpResponseNotFound("not found!")

    return render_to_response("article/a.html", {'obj': obj})


def about(request):
    return render_to_response("article/about.html")


def bate(request):
    return render_to_response("article/bate.html")


def tech(request):
    articles = ArticleModel.objects.order_by("-create_time").filter(status=0, article_type=0)
    articles = map(get_labels, articles)
    return render_to_response("article/tech.html", {"title": u"新技术", "articles": articles})


def test(request):
    articles = ArticleModel.objects.order_by("-create_time").filter(status=0, article_type=1)
    articles = map(get_labels, articles)
    return render_to_response("article/tech.html", {"title": u"技术测试", "articles": articles})


def data(request):
    articles = ArticleModel.objects.order_by("-create_time").filter(status=0, article_type=2)
    articles = map(get_labels, articles)
    return render_to_response("article/tech.html", {"title": u"资料分享", "articles": articles})


def baidu(request):
    return render_to_response("article/baidu.html")