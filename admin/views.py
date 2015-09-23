# coding:UTF-8


from django.shortcuts import render_to_response, redirect
from tech.models import ArticleModel, InfoModel
from glue.plug.ueditor import upload_file
import datetime
import hashlib
import time


def article(request, article_id):
    if request.method == "GET":
        if article_id == '0':
            obj = {'title': '', 'description': '', 'label': '', 'content': '', 'article_type': ''}
        else:
            obj = ArticleModel.objects.get(id=article_id)
        return render_to_response("admin/article.html", {'obj': obj, 'article_id': article_id})
    else:

        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        content = request.POST.get('content', None)
        article_type = request.POST.get('article_type', None)
        label = request.POST.get('label', None)

        #使用接口上传
        data = request.FILES['pic_url'].read()
        _, pic_url = upload_file(None, data)
        pic_url = "/pic/" + pic_url

        if article_id == '0':
            article_obj = ArticleModel(title=title, description=description, pic_url=pic_url, content=content,
                                       article_type=article_type, label=label, status=0,
                                       create_time=datetime.datetime.now())
            article_obj.save()
        else:
            ArticleModel.objects.filter(id=article_id).update(title=title, description=description, pic_url=pic_url,
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


def account(request):
    if request.method == "GET":
        return render_to_response("admin/account.html")
    else:

        user = InfoModel.objects.get(name='admin_username')
        passwd = InfoModel.objects.get(name='admin_password')

        if request.POST.get('username', None) == user.content and hashlib.md5(request.POST.get('password', None)).\
                hexdigest() == passwd.content:
            request.session['admin'] = time.time()

        return redirect("/admin/article/list")
