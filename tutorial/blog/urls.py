from django.conf.urls import url
from tutorial.blog import views
from tutorial.blog.views import index, indexHtml, addArticle, articlesCount, deleteArticle

urlpatterns = [
    url(r'^articles/$', views.article_list),
    url(r'^articlesapi/$', views.article_list_apiview),
    url(r'^addArticle/', addArticle),
    url(r'^articleCount/', articlesCount),
    url(r'^deleteArticle/', deleteArticle),
    url(r'^index/', index),
    url(r'^indexhtml', indexHtml),
]
