from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
# (https://office54.net/python/django/model-app-import)
from users.models import *

# Create your models here.
# 記事
class ArticleModel(models.Model):
    # 投稿者
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='投稿者', default=1)
    # 投稿内容
    posted_text = models.CharField(max_length=200,default="テキスト")
    # 投稿日時
    posted_at = models.DateTimeField(default=timezone.now(), blank=True)