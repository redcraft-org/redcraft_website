from django.http import HttpResponse
from django.views import View

from api_v1.Skin import Skin


class GetTemplateSkin(View):
    def get(self, request, username, *args, **kwargs):
        return HttpResponse(Skin(username).renderTemplate(), content_type="image/png")


class GetTemplateSkinScale(View):
    def get(self, request, username, size, *args, **kwargs):
        return HttpResponse(Skin(username).renderTemplate(size), content_type="image/png")


class GetHeadSkin(View):
    def get(self, request, username, *args, **kwargs):
        img = Skin(username).renderHead()
        return HttpResponse(img, content_type="image/png")


class GetHeadSkinScale(View):
    def get(self, request, username, size, *args, **kwargs):
        img = Skin(username).renderHead(size)
        return HttpResponse(img, content_type="image/png")


class GetBodySkin(View):
    def get(self, request, username, *args, **kwargs):
        img = Skin(username).renderBody()
        return HttpResponse(img, content_type="image/png")


class GetBodySkinScale(View):
    def get(self, request, username, size, *args, **kwargs):
        img = Skin(username).renderBody(size)
        return HttpResponse(img, content_type="image/png")
