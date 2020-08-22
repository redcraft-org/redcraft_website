from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from api_v1 import models as models_api_v1
from .service.DiscordService import DiscordService


class Home(TemplateView):
    template_name = 'website/pages/home.html'

    def get_context_data(self, **kwargs):

        discordService = DiscordService()

        return {
            'page': 'home',
            'discord': {
                'count_players_online': discordService.countPlayersOnline()
            },
            'minecraft_server': {
                'count_players_online': 69
            },
            'articles': [
                {
                    'title': 'Ouverture du faction',
                    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tincidunt massa.',
                    'url': '#',
                },
                {
                    'title': 'Event surprise de la semaine #12',
                    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                    'url': '#',
                },
                {
                    'title': 'Un nouveau site web !',
                    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam.',
                    'url': '#',
                },

            ]
        }


class Contact(TemplateView):
    template_name = 'website/pages/contact.html'

    def get_context_data(self, **kwargs):
        return {
            'page': 'contact',
            'menu_data' : {
                'exemple' : 1 ,
            },
        }


class Dons(TemplateView):
    template_name = 'website/pages/dons.html'

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
            query_url = models_api_v1.ReducedUrl.objects.get(shortened__exact=shortened)
        except ObjectDoesNotExist:
            return redirect('home')

        return redirect(query_url.url)
