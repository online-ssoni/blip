from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.http import Http404
import requests
import json
import random

#Views for Seminar

# clientID = '554726cc60d4d57a2f28a33ad9a521a0'
# clientSecret = 'a09eedfac27ed317c1b80822445a154118aef64e035f11d807c38f7a45c1f0df'


class Seminar(View):
    def get(self,request,seminar_token):
        rand_int = random.randint(0,1)
        if rand_int == 0 :
            return render(request, 'seminar/seminar.html')
        else:
            return render(request, 'seminar/seminar_host.html')
                
    def post(self, request, seminar_token):
        return HttpResponse('Hello');


def host(request):
    return render(request, 'seminar/seminar_host.html')

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



