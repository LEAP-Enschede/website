from django.http import Http404
from django.shortcuts import render
from datetime import datetime

from django.views import defaults

from news.models import Article, get_recent_articles
from events.models import Event, sync_events


def index(request):
    sync_events()
    news = get_recent_articles()
    # events = Event.objects.filter(start__gte=datetime.now())
    events = Event.objects.all()

    return render(request, 'home/index.html', {
        'news': news,
        'events': events,
    })
