from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from seminar.functions import check_host, get_event_attendees
import requests
import json
import random
from blip_core.models import Profile, Event, EventAttendees
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
from seminar.models import SeminarSession

#Views for Seminar

clientID = '554726cc60d4d57a2f28a33ad9a521a0'
clientSecret = 'a09eedfac27ed317c1b80822445a154118aef64e035f11d807c38f7a45c1f0df'

@login_required
def join(request, pk):
    seminar_token = pk
    context = {
        'seminar_token': seminar_token,
        'is_host': True
    }
    return render(request, 'events/join.html', context)


class Seminar(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Seminar, self).dispatch(request, *args, **kwargs)

    def get(self,request,seminar_token):
        participants_context = {}
        event_description = get_event_attendees(event_id=seminar_token)
        attendees = event_description['attendees']
        participants_context['event_description'] = Event.objects.get(pk=seminar_token)
        participants_context['is_host'] = check_host(request.user, event_id=seminar_token)
        participants_context['attendees'] = attendees
        participants_context['username'] = request.user.username
        if participants_context['is_host']:
            return render(request, 'seminar/seminar_host.html', {'participants_context': participants_context})
        else:
            if request.user.username in attendees:
                return render(request, 'seminar/seminar.html', {'participants_context': participants_context})
            else:
                return HttpResponse('Forbiddden')
    
    def post(self, request, seminar_token):
        event = Event.objects.get(pk=seminar_token)
        seminar_session = SeminarSession()
        seminar_session.event = event
        seminar_session.url = request.POST.get("url", "")
        seminar_session.seminar_token = seminar_token
        seminar_session.participant_count = 0
        seminar_session.save()
        return JsonResponse({'status':200}, safe=False)

@csrf_exempt
def run_program(request):
    
    data = {
        'clientId' : clientID,
        'clientSecret' : clientSecret,
        'script' : request.POST.get('script',''),
        'language' : 'python3',
        'versionIndex' : 1,
    };
    response = requests.post('https://api.jdoodle.com/v1/execute',json=data);

    return JsonResponse(response.json(), safe=False)
    


