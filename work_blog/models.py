from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
    author = models.CharField('автор статьи', max_length = 50)
    title = models.CharField('заголовок статьи', max_length = 100)
    text = models.TextField('текст статьи')
    created_date = models.DateTimeField(default = timezone.now())
    pub_date = models.DateTimeField(blank = True, null = True)
    def published(self):
        self.pub_date = timezone.now()
        self.save()
    def was_pub_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 5)
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author = models.CharField('автор комментария', max_length = 50)
    text = models.TextField('текст комментария')
    pub_date = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return self.author
