from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from blog.models import Article
from blog.serializers import AArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser


@csrf_exempt
def article_list(request):
    """
    list all articles
    :param request:
    :return:
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = AArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        article = AArticleSerializer(data=data)
        if article.is_valid():
            article.save()
            return JsonResponse(article.data, status=200)
        return JsonResponse(article.errors, status=400)


# Create your views here.

def index(request):
    a = {}
    a['name'] = '黄亚庆'
    a['age'] = 18
    return JsonResponse(a)


def indexHtml(request):
    print(request)
    return HttpResponse(Article.objects.all().count)


@api_view(['POST'])
def addArticle(request):
    print(request.data, request.scheme, request.auth)
    title = request.data["title"]
    a = Article(title=title)
    a.save()
    return HttpResponse("success" + str(a.id))


def articlesCount(request):
    articles = Article.objects.all()
    names = [{"title": i.title} for i in articles]
    return JsonResponse({"articles": names})


def deleteArticle(request):
    title = request.GET.get('title', '')
    for i in Article.objects.filter(title=title):
        i.delete()
    return HttpResponse('done')
