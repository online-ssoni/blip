from django.urls import path
from events.views import (create_event, join, upcoming_events,)


app_name = "events"

urlpatterns = [
    # path('', all_events, name='all_events'),
    path('new/', create_event, name='event-create'),
    path('join/<int:pk>/', join, name='join'),
    path('upcoming/', upcoming_events, name='upcoming_events'),
]
