from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blip_core.models import Profile, Event
from crispy_forms.helper import FormHelper
from django.contrib.admin import widgets   

from bootstrap_datepicker_plus import DateTimePickerInput
# class CreateEventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'description', 'start_time_date']

#         def __init__(self, *args, **kwargs):
#             super(CreateEventForm, self).__init__(*args, **kwargs)
#             self.fields['start_time_date'].widget = widgets.AdminSplitDateTime()

# class CreateEventForm(forms.ModelForm):
    
#     class Meta:
#         model = Event
#         fields = ['name', 'description', 'start_time_date']


#     def __init__(self, *args, **kwargs):
#         super(CreateEventForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget = widgets.AdminTextInputWidget()
#         self.fields['description'].widget = widgets.AdminTextareaWidget()
#         self.fields['start_time_date'].widget = widgets.AdminSplitDateTime()

# class DateInput(forms.DateTimeInput):
#     input_type = 'datetime'

class CreateEventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_time_date']
        widgets = {
            'start_time_date': DateTimePickerInput(),
        }