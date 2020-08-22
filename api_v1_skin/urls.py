from django.urls import path
from api_v1_skin import views


urlpatterns = [
    path('skin/template/<str:ref>', views.getTemplateSkin, name='get_skin_template'),
    path('skin/head/<str:ref>', views.getHeadSkin, name='get_skin_head'),
    path('skin/body/<str:ref>', views.getBodySkin, name='get_skin_body'),
]
