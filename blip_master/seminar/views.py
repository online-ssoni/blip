from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.http import Http404
import requests
import json
import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blip_core.models import Profile, Event, EventAttendees
from datetime import datetime

#Views for Seminar

# clientID = '554726cc60d4d57a2f28a33ad9a521a0'
# clientSecret = 'a09eedfac27ed317c1b80822445a154118aef64e035f11d807c38f7a45c1f0df'
def check_host(user, event_id):
    q = Event.objects.get(pk=event_id).host
    if q.username == user.username:
        return True 
    else:
        return False

class Seminar(View):
    # def __init__(self):
    #     self.participants_context = {}
        
    #     participants_context['is_host'] = True


    # def get(self,request,seminar_token):
    #     rand_int = random.randint(0,1)
    #     if rand_int == 0 :
    #         return render(request, 'seminar/seminar.html', {'participants_context': self.participants_context})
    #     else:
    #         return render(request, 'seminar/seminar_host.html', {'participants_context': self.participants_context})
                
    def get(self,request,seminar_token):
        participants_context = {}
        attendees = get_event_attendees(event_id=seminar_token) 
        participants_context['is_host'] = check_host(request.user, event_id=seminar_token)
        participants_context['attendees'] = attendees

        if participants_context['is_host']:
            return render(request, 'seminar/seminar_host.html', {'participants_context': participants_context})
        else:
            if request.user.username in attendees:
                return render(request, 'seminar/seminar.html', {'participants_context': participants_context})
            else:
                return HttpResponse('Forbidden:403')
    def post(self, request, seminar_token):
        return HttpResponse('Hello');

def get_event_attendees(event_id):
    attendees = EventAttendees.objects.filter(event__id=event_id)
    attendees_usernames = []
    for attendee in attendees:
        attendees_usernames.append(attendee.user.username)
    return attendees_usernames





@login_required
def join(request, pk):
    seminar_token = pk
    context = {
        'seminar_token': seminar_token,
        'is_host': True
    }
    return render(request, 'events/join.html', context)


# def host(request):
#     return render(request, 'seminar/seminar_host.html')

# def run_program(request):
#     data = {
#         'clientId' : clientID,
#         'clientSecret' : clientSecret,
#         'script' : "print('hello')",
#         'language' : 'python3',
#         'versionIndex' : 1,
#     };
#     print(data)
#     response = requests.post('https://api.jdoodle.com/v1/execute',json=data);
   
#     return JsonResponse(response.json(), safe=False)



