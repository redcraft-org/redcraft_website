from django.urls import path

from api_v1_article import views


urlpatterns = [
    path('', views.getArticles, name='get_list_article'),
    path('<str:language>/<int:id>-<str:slug>', views.getArticle, name='get_article_with_slug'),
    path('<str:language>/<int:id>', views.getArticle, name='get_article'),
]
