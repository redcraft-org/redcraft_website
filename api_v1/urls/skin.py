from django.urls import path

from api_v1.views import skin


urlpatterns = [
    path('skin/template/<str:ref>', skin.GetTemplateSkin.as_view(), name='get_skin_template'),
    path('skin/template/<str:ref>/<int:size>', skin.GetTemplateSkinScale.as_view(), name='get_skin_template_size'),
    path('skin/head/<str:ref>', skin.GetHeadSkin.as_view(), name='get_skin_head'),
    path('skin/head/<str:ref>/<int:size>', skin.GetHeadSkinScale.as_view(), name='get_skin_head_size'),
    path('skin/body/<str:ref>', skin.GetBodySkin.as_view(), name='get_skin_body'),
    path('skin/body/<str:ref>/<int:size>', skin.GetBodySkinScale.as_view(), name='get_skin_head_body'),
]
