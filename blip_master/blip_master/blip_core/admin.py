from django.contrib import admin
from blip_core.models import Profile, Event, EventAttendees
# Register your models here.

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(EventAttendees)