# coding:UTF-8

from django.conf.urls import url, patterns


urlpatterns = patterns('admin.views',
    url(r'^article/(?P<article_id>)', 'article'),
)