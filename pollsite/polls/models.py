import datetime

from django.db import models
from django.utils import timezone

#Question class inherits properties of models.Model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    #ForeignKey defines relationship- tells django each choice is related to a single question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #CharField tells it what kind of data to expect and also take a max len arg
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

