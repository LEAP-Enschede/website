from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    news = Article.objects.all()
    return render(request, 'news/index.html', {
        'news': news
    })


def article(request, news_id):
    news = get_object_or_404(Article, pk=news_id)
    return render(request, 'news/article.html', {
        'article': news
    })