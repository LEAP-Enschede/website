from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField('published_at')
    image = models.ImageField(upload_to='news')

    def __str__(self):
        return self.title


def get_recent_articles():
    relevant_date = datetime.now() - relativedelta(months=1)
    return Article.objects.filter(published_at__gte=relevant_date)
