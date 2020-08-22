from django.urls import path

from api_v1_url import views


urlpatterns = [
    path('urls', views.GetUrlList.as_view(), name='get_urls'),
    path('url', views.SetUrl.as_view(), name='set_url'),
]
