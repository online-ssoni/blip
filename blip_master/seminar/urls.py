from django.urls import path
from seminar.views import Seminar, join


app_name = "seminar"
urlpatterns = [
    path('seminar_dashboard/<slug:seminar_token>/', Seminar.as_view(), name='seminar_dashboard'),
    # path('run/', run_program, name='run'),
    path('join/<int:pk>/', join, name='join'),
]
