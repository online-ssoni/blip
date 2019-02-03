from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField()
    is_active = models.BooleanField(default=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not prefer to say')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at = models.DateField(auto_now_add=True)


class Event(models.Model):
   name = models.CharField(max_length=40, blank=False)
   description = models.TextField(max_length=500, blank=False)
   host = models.ForeignKey(User, on_delete=models.CASCADE)
   start_time_date = models.DateTimeField(auto_now=True)
   created_at = models.DateTimeField(auto_now_add=True)
   last_modified_at = models.DateTimeField(blank=True)
   expired_status = models.BooleanField(default=False)


class EventAttendees(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blocked_status = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
   if created:
       Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.profile.save()