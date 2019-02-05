from django.shortcuts import render, redirect
from home.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blip_core.models import Profile, Event, EventAttendees
from datetime import datetime 
# Create your views here.

def index(request):

    events = Event.objects.all()
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
    return render(request, 'home/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'profile/register.html', {'form': form})


@login_required
def profile(request):
    events_attended_count = 0
    upcoming_events_count = 0
    all_events = Event.objects.all()
    for key in all_events:
        if key.start_time_date.isoformat() >= datetime.now().isoformat():
            upcoming_events_count += 1

    all_events_attended = list(EventAttendees.objects.filter(id=request.user.id))
    events_attended_count = len(all_events_attended)
    events_created = len(list(EventAttendees.objects.filter(pk=(request.user.id))))
    context = {
        'username': request.user.username,
        'created_at': Profile.objects.get(pk=request.user.profile.id).created_at,
        'bio': Profile.objects.get(pk=request.user.profile.id).bio,
        'email': request.user.email,
        'gender': Profile.objects.get(pk=request.user.profile.id).gender,
        'upcoming_events': upcoming_events_count,
        'events_attended_count': events_attended_count,
        'events_created':events_created,
    }

    return render(request, 'profile/profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'profile/update_profile.html', context)