from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    """文章标签"""
    text = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text

class Category(models.Model):
    """文章分类"""
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
class Article(models.Model):
    # 分类
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )

    # 标题
    title = models.CharField(max_length=100)
    # 正文
    body = models.TextField()
    # 作者
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        # 表名
        db_table = 'article'
        ordering = ['-created']
    def __str__(self):
        return self.title

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles'
    )
