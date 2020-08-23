from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from api_v1 import models as models_api_v1
from .service.DiscordService import DiscordService
from api_v1_article.service.ArticleService import ArticleService


class BaseViewFrontEnd(TemplateView):
    def get_context_data(self, **kwargs):
        return {
            'links' : {
                'twitter' : '#',
                'facebook' : 'https://fb.me/RedCraftorg',
                'youtube' : 'https://www.youtube.com/channel/UClo30bzHPYHz847o5WlfE6g',
                'discord' : 'https://discord.gg/h9SfJmh',
                'instagram' : 'https://www.instagram.com/redcraftorg',
            }
        }


class Home(BaseViewFrontEnd):
    template_name = 'website/pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()

        discord_service = DiscordService()
        article_service = ArticleService()
        

        return {
            **ctx,
            **{
                'page': 'home',
                'discord': {
                    'count_players_online': discord_service.countPlayersOnline()
                },
                'minecraft_server': {
                    'count_players_online': 69,
                    'ip_address': 'play.redcraft.org',
                },
                'articles': article_service.getLastArticle(3),
            }
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
