from django.urls import path, re_path

from api_v1_article import views


urlpatterns = [
    path('', views.getArticles, name='get_list_article'),
    re_path(r'^(?P<id>[0-9]{1,8})-(?P<language>[a-z]{2})-(?P<slug>[\w-]+)', views.getArticle, name='get_article_with_slug'),
    re_path(r'^(?P<id>[0-9]{1,8})-(?P<language>[a-z]{2})', views.getArticle, name='get_article'),
]
