from django.db import models
from django.core import validators

class Route(models.Model):
    route = models.IntegerField(
        verbose_name='路線ID'
    )
    route_name = models.CharField(
        verbose_name='路線名',
        max_length=20,
        default=''
    )

    def __str__(self):
        return self.route_name
    class Meta:
        verbose_name = '路線'
        verbose_name_plural = '路線'
    

class Item(models.Model):

    name = models.CharField(
        verbose_name='列車名',
        max_length=200
    )
    route = models.ManyToManyField(
        Route,
        verbose_name='所属路線',
        default=1
    )
    thumnail = models.ImageField(
        verbose_name='画像',
        upload_to = 'images',
        blank=True,
        null=True
    )
    memo = models.TextField(
        verbose_name='説明',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # ↓↓管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '列車'
        verbose_name_plural = '列車'