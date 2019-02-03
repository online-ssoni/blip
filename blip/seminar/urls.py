from django.urls import path
from seminar.views import Seminar

urlpatterns = [
    path('seminar_dashboard/<slug:seminar_token>/', Seminar.as_view(), name='seminar_dashboard'),
    # path('run/', run_program, name='run'),
]
