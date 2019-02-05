from django.db import models
from blip_core.models import Event


#Models for Seminar App
class SeminarSession(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    seminar_token = models.CharField(max_length=64, unique=True, default='dxyxxxxsjakj')
    participant_count = models.IntegerField(default=0)


class CodeSnippet(models.Model):
    LANGUAGE_CHOICES = (('js','JavaScript '),
     ('php','PHP'),('xml','XML'),('py','Python'))
    session = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    snippet = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)


