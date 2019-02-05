from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_active = models.BooleanField(default=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not prefer to say')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    bio = models.CharField(max_length=500, default='This is default bio')

    def __str__(self):
        return self.user.username
    
    def save(self, force_insert=False, force_update=False, using=None):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

        

class Event(models.Model):
    name = models.CharField(max_length=40, blank=False)
    description = models.TextField(max_length=500, blank=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now_add=True)
    expired_status = models.BooleanField(default=False)
    
    def save(self, force_insert=False, force_update=False, using=None): 
        super().save()
    
    def __str__(self):
        return self.name

class EventAttendees(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blocked_status = models.BooleanField(default=False)
    attended_status = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None):
        super().save()
    
    

