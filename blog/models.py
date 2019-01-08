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
    commentuser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    commentarticle = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentcontent = models.TextField()
    commenttime = models.DateTimeField(default=timezone.now)
    commentexist = models.IntegerField(default=1)

    def __str__(self):
        return (
                '评论人：%s，评论文章：%s，评论内容：%s，评论是否存在：%d'
                % (self.commentuser, self.commentarticle, self.commentcontent, self.commentexist)
        )


class Likeit(models.Model):
    likeituser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    likeitarticle = models.ForeignKey('Post', on_delete=models.CASCADE)
    likeittime = models.DateTimeField(default=timezone.now)
    likeitexist = models.IntegerField(default=0)

    def __str__(self):
        return (
                '点赞人：%s，点赞文章：%s，点赞时间：%s，点赞是否存在：%d'
                % (self.likeituser, self.likeitarticle, str(self.likeittime), self.likeitexist)
        )