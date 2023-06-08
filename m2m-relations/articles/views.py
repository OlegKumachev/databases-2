from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    articles = Article.objects.order_by('-published_at')
    template = 'articles/news.html'
    context = {'articles': articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
