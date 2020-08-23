from django.urls import path

from api_v1_article import views


urlpatterns = [
    path('', views.getArticles, name='get_list_article'),
    path('<int:id>-<str:language>-<str:slug>', views.getArticle, name='get_article_with_slug'),
    path('<int:id>-<str:language>', views.getArticle, name='get_article'),
]
