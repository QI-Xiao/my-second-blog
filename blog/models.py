from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # null    如果值为True, 在数据库中Django将把空值储存为Null。默认值为False。
    # blank   如果值为True, 字段允许为空。默认值为False

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    article = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return (
                '评论人：%s，评论文章：%s，评论内容：%s，评论是否删除：%s'
                % (self.user, self.article, self.content, self.isdelete)
        )


class Likeit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    article = models.ForeignKey('Post', on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return (
                '点赞人：%s，点赞文章：%s，点赞时间：%s，点赞是否取消：%s'
                % (self.user, self.article, str(self.time), self.isdelete)
        )