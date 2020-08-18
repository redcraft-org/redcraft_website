from django.urls import path

from website import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('contact.html', views.Contact.as_view(), name='contact'),
    path('dons.html', views.Dons.as_view(), name='dons'),
    path('skin.html', views.Skin.as_view(), name='skin'),
    path('r/<str:shortened>', views.UrlReducer.as_view(), name='url_reducer'),
]
