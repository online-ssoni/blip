from blip_core.models import Profile, Event, EventAttendees

def check_host(user, event_id):
    q = Event.objects.get(pk=event_id).host
    if q.username == user.username:
        return True 
    else:
        return False

def get_event_attendees(event_id):
    attendees = EventAttendees.objects.filter(event__id=event_id)
    attendees_usernames = []
    for attendee in attendees:
        attendees_usernames.append(attendee.user.username)
    return attendees_usernames