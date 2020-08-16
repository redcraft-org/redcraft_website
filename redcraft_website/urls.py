from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),

    path('api/v1/skin/', include('api_v1_skin.urls')),
    path('api/v1/url/', include('api_v1_url.urls')),
]
