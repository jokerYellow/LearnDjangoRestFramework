from django.conf.urls import url, include
from blog import views
from blog.views import index, indexHtml, addArticle, articlesCount, deleteArticle

urlpatterns = [
    url(r'^articles/$', views.article_list),
    url(r'^addArticle/', addArticle),
    url(r'^articleCount/', articlesCount),
    url(r'^deleteArticle/', deleteArticle),
    url(r'^index/', index),
    url(r'^indexhtml', indexHtml),
]
