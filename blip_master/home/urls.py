from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (index, register, profile, update_profile, profile_dashboard)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='blip-home'),
    path('login/',auth_views.LoginView.as_view(template_name='profile/login.html'), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('update_profile', update_profile, name='update_profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profile/logout.html'), name='logout'),
    path('events/', include('events.urls', namespace='events')),
    path('profile_dashboard/', profile_dashboard, name='profile_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
