from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/1.html', {'articles': articles})

def get_article_by_id(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/2.html', {'article': article})