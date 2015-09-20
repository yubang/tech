# coding:UTF-8


from django.shortcuts import render_to_response
from tech.models import ArticleModel


def index(request):
    return render_to_response("article/index.html")


def content(request, article_id):
    return render_to_response("article/a.html",{})


def about(request):
    return render_to_response("article/about.html")


def bate(request):
    return render_to_response("article/bate.html")


def tech(request):
    articles = ArticleModel.objects.order_by("-create_time").filter(status=0, description=0)
    return render_to_response("article/tech.html", {"articles": articles})


def test(request):
    return render_to_response("article/tech.html", {"articles": range(1, 2)})