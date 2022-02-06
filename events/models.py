from django.db import models
import requests
from icalendar import Calendar


def sync_events():
    r = requests.get(
        'https://calendar.google.com/calendar/ical/732bmjkmmc4u5kok9bso13jai4%40group.calendar.google.com/public/basic.ics')
    cal = Calendar.from_ical(r.text)
    events = [{
        'uid': event.decoded('uid').decode('UTF-8'),
        'title': event.decoded('summary').decode('UTF-8'),
        'description': event.decoded('description').decode('UTF-8'),
        'location': event.decoded('location').decode('UTF-8'),
        'start': event.decoded('dtstart'),
        'end': event.decoded('dtend'),
        'last_modified': event.decoded('last-modified'),
    } for event in cal.walk('vevent')]

    for event in events:
        query = Event.objects.filter(pk=event['uid'])
        if query.exists():
            db_event = query.get()
            if event['last_modified'] == db_event.last_modified:
                continue
        else:
            db_event = Event()

        db_event.uid = event['uid']
        db_event.title = event['title']
        db_event.description = event['description']
        db_event.location = event['location']
        db_event.start = event['start']
        db_event.end = event['end']
        db_event.last_modified = event['last_modified']
        db_event.save()

    uid_list = [event['uid'] for event in events]

    for db_event in Event.objects.all():
        if db_event.uid not in uid_list:
            db_event.delete()


class Event(models.Model):
    uid = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')
    last_modified = models.DateTimeField('last_modified')

    def __str__(self):
        return self.title
