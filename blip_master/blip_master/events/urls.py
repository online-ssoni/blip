from django.urls import path
from events.views import (create_event, upcoming_events,)


app_name = "events"

urlpatterns = [
    # path('', all_events, name='all_events'),
    path('new/', create_event, name='event-create'),

    path('upcoming/', upcoming_events, name='upcoming_events'),
]
