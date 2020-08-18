from django.urls import path

from api import views


urlpatterns = [
    path('', views.GetStocksList.as_view(), name='get_urls'),
    path('<str:shortened>', views.GetStocksList.as_view(), name='get_url'),
]
