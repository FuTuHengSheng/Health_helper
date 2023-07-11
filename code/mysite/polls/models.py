import datetime#时区

from django.db import models
from django.utils import timezone#时区
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #存储问题的文本信息
    pub_date = models.DateTimeField("date published")
    #存储问题的发布日期和时间。
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #存储该选项的投票数，默认值为0。
    def __str__(self):
        return self.choice_text
    

