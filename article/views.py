# coding:UTF-8


from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from tech.models import ArticleModel


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
    return render_to_response("article/index.html")


def content(request, article_id):
    try:
        obj = ArticleModel.objects.get(id=article_id)
        obj = get_labels(obj)
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
    return render_to_response("article/tech.html", {"articles": articles})


def test(request):
    articles = ArticleModel.objects.order_by("-create_time").filter(status=0, article_type=1)
    articles = map(get_labels, articles)
    return render_to_response("article/tech.html", {"articles": articles})