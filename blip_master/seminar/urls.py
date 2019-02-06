from django.urls import path
from seminar.views import Seminar, join, run_program, check_live, save_file


app_name = "seminar"
urlpatterns = [
    path('seminar_dashboard/<slug:seminar_token>/', Seminar.as_view(), name='seminar_dashboard'),
    path('run/', run_program, name='run'),
    path('join/<int:pk>/', join, name='join'),
    path('save/', save_file, name='save'),
    path('check_live/<int:event_id>', check_live, name='check_live'),
]
