from django.urls import path
from events.views import (exit_events, create_event, upcoming_events, subscribe, events_created)


app_name = "events"

urlpatterns = [
    # path('', all_events, name='all_events'),
    path('new/', create_event, name='event-create'),
    path('subscribe/<int:seminar_token>/', subscribe, name='subscribe'),
    path('upcoming/', upcoming_events, name='upcoming_events'),
    path('created/', events_created, name='events_created'),
    path('exit/', exit_events, name='exit_events'),
]
