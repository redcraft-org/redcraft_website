from django.views.generic.base import TemplateView


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


class UrlReducer(TemplateView):
    template_name = "website/pages/url_reducer.html"

    def get_context_data(self, **kwargs):
        return {
            'page': 'url_reducer',
            'menu_data' : {
                'exemple' : 1 ,
            },
        }


class Skin(TemplateView):
    template_name = "website/pages/skin.html"

    def get_context_data(self, **kwargs):
        return {
            'page': 'skin',
            'menu_data' : {
                'exemple' : 1 ,
            },
        }
