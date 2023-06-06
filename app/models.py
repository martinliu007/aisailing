from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# 文章列表 model
class App(models.Model):
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