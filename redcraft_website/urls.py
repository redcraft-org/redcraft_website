from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),

    path('api/v1/', include('api_v1.urls')),
    path('api/v1/articles/', include('api_v1_article.urls')),
]
