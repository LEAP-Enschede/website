from django.shortcuts import render, get_object_or_404
from datetime import datetime

from .models import sync_events, Event


def index(request):
    sync_events()

    upcoming = Event.objects.filter(start__gte=datetime.today()).order_by('start')
    past = Event.objects.filter(start__lt=datetime.today()).order_by('start')

    return render(request, 'events/index.html', {
        'upcoming': upcoming,
        'past': past,
    })


def detail(request, event_uid):
    event = get_object_or_404(Event, pk=event_uid)

    return render(request, 'events/detail.html', {
        'event': event,
    })
