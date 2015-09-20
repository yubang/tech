# coding:UTF-8


from django.shortcuts import render_to_response



def article(request, article_id):
    return render_to_response("admin/article.html")