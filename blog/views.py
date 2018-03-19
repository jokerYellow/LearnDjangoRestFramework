from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from blog.models import Article


# Create your views here.

def index(request):
    a = {}
    a['name'] = '黄亚庆'
    a['age'] = 18
    return JsonResponse(a)


def indexHtml(request):
    print(request)
    return HttpResponse(Article.objects.all().count)


def addArticle(request):
    title = request.GET.get('title', '')
    a = Article(title=title)
    a.save()
    return HttpResponse("success")


def articlesCount(request):
    articles = Article.objects.all()
    names = [{"title": i.title} for i in articles]
    return JsonResponse({"articles": names})

def deleteArticle(request):
    title = request.GET.get('title', '')
    for i in  Article.objects.filter(title=title):
        i.delete()
    return HttpResponse('done')