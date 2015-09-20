# coding:UTF-8

from django.db import models


class ArticleModel(models.Model):
    """
    文章类
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    content = models.TextField()
    article_type = models.SmallIntegerField()
    label = models.CharField(max_length=30)
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = "tech_article"


class InfoModel(models.Model):
    """
    信息类
    """
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    create_time = models.DateTimeField()

    class Meta:
        db_table = "tech_info"
