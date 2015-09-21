# coding:UTF-8


from django.shortcuts import render_to_response, redirect
from tech.models import ArticleModel
import datetime


def article(request, article_id):
    if request.method == "GET":
        if article_id == '0':
            obj = {}
        else:
            obj = ArticleModel.objects.get(id=article_id)
        return render_to_response("admin/article.html", {'obj': obj})
    else:

        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        # pic_url = request.POST.get('pic_url', None)
        content = request.POST.get('content', None)
        article_type = request.POST.get('article_type', None)
        label = request.POST.get('label', None)

        if article_id == '0':
            article_obj = ArticleModel(title=title, description=description, pic_url='', content=content,
                                       article_type=article_type, label=label, status=0,
                                       create_time=datetime.datetime.now())
            article_obj.save()
        else:
            ArticleModel.objects.filter(id=article_id).update(title=title, description=description, pic_url='',
                                                              content=content,article_type=article_type, label=label,
                                                              status=0, create_time=datetime.datetime.now())
        return redirect("/admin/article/list")


def list(request):
    """
    文章列表
    :param request:
    :return:
    """
    articles = ArticleModel.objects.order_by("-id").filter(status__lt=2)
    return render_to_response("admin/list.html", {"articles": articles})


def status(request, article_id, article_status):
    ArticleModel.objects.filter(id=article_id).update(status=article_status)
    return redirect("/admin/article/list")