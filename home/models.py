from django.db import models
from django.urls import reverse
from pages.models import Page


class MenuItem(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='menu_items', blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    route = models.CharField(max_length=20, blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField()

    def get_url(self):
        if self.page:
            return reverse('pages:page', args=[self.page.url])
        elif self.route:
            return reverse(self.route)
        else:
            return self.url

    def has_children(self):
        return len(self.menu_items.all()) > 0

    def __str__(self):
        name = self.name
        if self.parent:
            name = self.parent.name + '->' + name
        return name
