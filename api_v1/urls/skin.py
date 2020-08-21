from django.urls import path

from api_v1.views import skin


urlpatterns = [
    # Template
    path('skin/template/<str:ref>', skin.getTemplateSkin, name='get_skin_template'),
    # Head
    path('skin/head/<str:ref>', skin.getHeadSkin, name='get_skin_head'),
    # Body
    path('skin/body/<str:ref>', skin.getBodySkin, name='get_skin_body'),
]
