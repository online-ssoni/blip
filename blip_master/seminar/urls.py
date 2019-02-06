from django.urls import path
from seminar.views import Seminar, join, run_program, save_file


app_name = "seminar"
urlpatterns = [
    path('seminar_dashboard/<slug:seminar_token>/', Seminar.as_view(), name='seminar_dashboard'),
    path('run/', run_program, name='run'),
    path('save/', save_file, name='save'),
    path('join/<int:pk>/', join, name='join'),
]
