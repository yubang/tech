# coding:UTF-8

from django.conf.urls import url, patterns


urlpatterns = patterns('admin.views',
    url(r'^account', 'account'),
    url(r'^article/(?P<article_id>\d+)', 'article'),
    url(r'^article/list$', 'list'),
    url(r'^article/status/(?P<article_id>\d+)/(?P<article_status>\d+)$', 'status'),
)