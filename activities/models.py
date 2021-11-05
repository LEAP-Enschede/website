from django.db import models
from django.utils import timezone


class Activity(models.Model):
    name = models.CharField(max_length=200)
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')

    def has_past(self):
        return self.end < timezone.now()

    def __str__(self):
        return self.name


class ActivitySignup(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    max_participants = models.IntegerField('max participants')
    start = models.DateTimeField('signup start')
    end = models.DateTimeField('signup end')

    def __str__(self):
        return self.activity.name
