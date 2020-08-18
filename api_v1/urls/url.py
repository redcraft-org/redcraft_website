from django.urls import path

from api_v1.views import url


urlpatterns = [
    path('urls', url.GetUrlList.as_view(), name='get_urls'),
    path('url', url.SetUrl.as_view(), name='set_url'),
]
