from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blip_core.models import Profile
from crispy_forms.helper import FormHelper


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio' ,'gender']

