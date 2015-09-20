# coding:UTF-8


from django.conf.urls import url, patterns


urlpatterns = patterns('article.views',
    url(r'^$', 'index'),
    url(r'^a/(?P<article_id>\d+)', 'content'),
)