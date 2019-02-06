from django.db import models
from blip_core.models import Event
from django.contrib.auth.models import User

#Models for Seminar App
class SeminarSession(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    seminar_token = models.CharField(max_length=64, unique=True, default='dxyxxxxsjakj')
    participant_count = models.IntegerField(default=0)


class CodeSnippet(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    snippet = models.TextField()
    language = models.CharField(max_length=10)
    extension = models.CharField(max_length=5, default='py')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


