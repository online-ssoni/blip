
from django.shortcuts import render, redirect
from events.forms import CreateEventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blip_core.models import Profile, Event, EventAttendees
from datetime import datetime
from home.views import index

@login_required
def create_event(request):
    if request.method == 'POST':
        event_form = CreateEventForm(request.POST)
        if event_form.is_valid():
            candidate = event_form.save(commit=False)
            candidate.host_id = request.user.id
            candidate.save()
            subscribe(request, candidate.id)
            return redirect('profile')
    else:
        event_form = CreateEventForm(instance=request.user)
    context = {'event_form': event_form,}
    return render(request, 'events/event_form.html', context)

# @login_required
# def join(request, pk):
#     return render(request, 'seminar.views.Seminar.as_view()', seminar_token='safsdf' )



@login_required
def upcoming_events(request):
    events = Event.objects.filter(start_time_date__gte=datetime.now())
    events_context = []
    for event in events:
        current_context = {}
        current_context['event_id'] = event.id
        current_context['event_name'] = event.name 
        current_context['event_description'] = event.description
        current_context['host'] = event.host.username
        current_context['starts_in'] = event.start_time_date
        events_context.append(current_context)
    context = {'events': events_context}
    return render(request, 'events/upcoming_events.html', context)

@login_required
def events_created(request):
    events = Event.objects.filter(start_time_date__gte=datetime.now())
    events = Event.objects.filter(host=request.user)
    events_context = []
    for event in events:
        current_context = {}
        current_context['event_id'] = event.id
        current_context['event_name'] = event.name 
        current_context['event_description'] = event.description
        current_context['host'] = event.host.username
        current_context['starts_in'] = event.start_time_date
        events_context.append(current_context)
    context = {'events': events_context}
    return render(request, 'events/events_created.html', context)

@login_required
def subscribe(request, seminar_token):
    subscription = EventAttendees(event=Event.objects.get(pk=seminar_token),user=request.user)
    subscription.save()
    return redirect(index)


def exit_events(request):
    return redirect(index)