from django.http import HttpResponse
from django.views import View

from api_v1.Skin import Skin


class GetTemplateSkin(View):
    def get(self, request, ref, *args, **kwargs):
        return HttpResponse(Skin(ref).renderTemplate(), content_type="image/png")


class GetTemplateSkinScale(View):
    def get(self, request, ref, size, *args, **kwargs):
        return HttpResponse(Skin(ref).renderTemplate(size), content_type="image/png")


class GetHeadSkin(View):
    def get(self, request, ref, *args, **kwargs):
        img = Skin(ref).renderHead()
        return HttpResponse(img, content_type="image/png")


class GetHeadSkinScale(View):
    def get(self, request, ref, size, *args, **kwargs):
        img = Skin(ref).renderHead(size)
        return HttpResponse(img, content_type="image/png")


class GetBodySkin(View):
    def get(self, request, ref, *args, **kwargs):
        img = Skin(ref).renderBody()
        return HttpResponse(img, content_type="image/png")


class GetBodySkinScale(View):
    def get(self, request, ref, size, *args, **kwargs):
        img = Skin(ref).renderBody(size)
        return HttpResponse(img, content_type="image/png")
