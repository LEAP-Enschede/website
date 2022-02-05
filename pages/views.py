from django.shortcuts import render, get_object_or_404
from .models import Page


def page(request, page_url):
    page_object = get_object_or_404(Page, url=page_url)

    return render(request, 'pages/page.html', {
        'page': page_object,
    })
