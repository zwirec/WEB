from django.db import models

class Answer(models.Model):
    text = models.TextField()
    is_correct = models.NullBooleanField()


class Question(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    rate = models.IntegerField()
    pub_date = models.DateTimeField()
    answers = models.ManyToManyField(Answer)
