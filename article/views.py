# coding:UTF-8


from django.shortcuts import render_to_response


def index(request):
    return render_to_response("article/index.html")


def content(request, article_id):
    return render_to_response("article/a.html",{})


def about(request):
    return render_to_response("article/about.html")


def bate(request):
    return render_to_response("article/bate.html")
