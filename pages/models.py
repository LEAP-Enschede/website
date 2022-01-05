from django.db import models


class Page(models.Model):
    url = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
