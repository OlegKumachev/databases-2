from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    articles = Article.objects.order_by('-published_at')
    template = 'articles/news.html'
    context = {'articles': articles}


    return render(request, template, context)
