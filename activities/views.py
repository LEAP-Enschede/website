from django.shortcuts import render, get_object_or_404

import requests
from icalendar import Calendar

from .models import Activity


def index(request):
    activities = Activity.objects.all()

    return render(request, 'activities/index.html', {
        'activities': activities,
    })


def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    return render(request, 'activities/detail.html', {
        'activity': activity,
    })
