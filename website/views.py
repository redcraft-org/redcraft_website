from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from api_v1_url import models as models_api_url_v1


class Home(TemplateView):
    template_name = "website/pages/home.html"

    def get_context_data(self, **kwargs):
        return {
            'page': 'home',
            'menu_data' : {
                'exemple' : 1 ,
            },
        }


class Contact(TemplateView):
    template_name = "website/pages/contact.html"

    def get_context_data(self, **kwargs):
        return {
            'page': 'contact',
            'menu_data' : {
                'exemple' : 1 ,
            },
        }


class Dons(TemplateView):
    template_name = "website/pages/dons.html"

    def get_context_data(self, **kwargs):
        return {
            'page': 'dons',
            'menu_data' : {
                'exemple' : 1 ,
            },
        }


class UrlReducer(View):
    def get(self, request, shortened, *args, **kwargs):
        try:
            query_url = models_api_url_v1.ReducedUrl.objects.get(shortened__exact=shortened)
        except ObjectDoesNotExist:
            return redirect('home')

        return redirect(query_url.url)


class Skin(TemplateView):
    template_name = "website/pages/skin.html"

    def get_context_data(self, **kwargs):
        return {
            'page': 'skin',
            'menu_data' : {
                'exemple' : 1 ,
            },
        }
