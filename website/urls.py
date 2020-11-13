from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from website import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('vote.html', views.Vote.as_view(), name='vote'),
    path('dons.html', views.Dons.as_view(), name='dons'),
    path('stats.html', views.Stats.as_view(), name='stats'),
    path('rules.html', views.Rules.as_view(), name='rules'),
    path('contact.html', views.Contact.as_view(), name='contact'),
    path('articles.html', views.Articles.as_view(), name='articles'),
    path('livemap.html', views.Livemap.as_view(), name='livemap'),
    path('about.html', views.About.as_view(), name='about'),
    path('r/<str:shortened>', views.UrlReducer.as_view(), name='url_reducer'),
]

urlpatterns += staticfiles_urlpatterns()
