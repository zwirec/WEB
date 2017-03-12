# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    questions = models.ManyToManyField('Question', related_name='tags')
    count = models.IntegerField()

    def __str__(self):
        return self.name

    def add_count(self):
        self.count += 1


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="uploads/", verbose_name='Images')

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.user.username


class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField()
    pub_date = models.DateTimeField(null=True)
    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.text[:20]

    def __str__(self):
        return self.text[:20]


class Question(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    rate = models.IntegerField()
    pub_date = models.DateTimeField(null=True)
    answers = models.OneToOneField(Answer, blank=True, null=True)
    user_that_makes_it = models.ForeignKey(UserProfile, related_name='questions', null=True)

    def add_rate(self):
        self.rate += 1

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
