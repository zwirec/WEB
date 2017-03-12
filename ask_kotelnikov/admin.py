# -*- coding: utf-8 -*-
from django.contrib import admin

from ask_kotelnikov.models import Question, Answer, UserProfile, Tag

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserProfile)
admin.site.register(Tag)