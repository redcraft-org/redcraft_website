from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from api_v1_url import models as models_api_url_v1
from .service.DiscordService import DiscordService
from api_v1_article.service.ArticleService import ArticleService
from network_data.service.NetworkDescriptionService import NetworkDescriptionService
from network_data.service.ServerDescriptionService import ServerDescriptionService


class BaseViewFrontEnd(TemplateView):
    def get_context_data(self, **kwargs):
        return {
            'links' : {
                'twitter' : 'https://twitter.com/RedCraftorg',
                'facebook' : 'https://fb.me/RedCraftorg',
                'github' : 'https://github.com/redcraft-org',
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
        network_description_service = NetworkDescriptionService()
        server_description_service = ServerDescriptionService()

        return {
            **ctx,
            **{
                'page': 'home',
                'discord': {
                    'count_players_online': discord_service.countPlayersOnline()
                },
                'minecraft_server': {
                    'count_players_online': 69420,
                    'ip_address': 'play.redcraft.org',
                },
                'articles': article_service.getLastArticle(3),
                
                'network_presentations': network_description_service.getAllActive(),
                'servers_list': server_description_service.getAllActive(),
                'staff_list': [
                    {
                        'name': 'lululombard',
                        'path_img' : 'http://127.0.0.1:8000/api/v1/skin/head/lululombard?size=300',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url' : 'https://twitter.com/lululombard',
                                'logo_fa' : 'twitter'
                            },
                            {
                                'name': 'YouTube',
                                'url' : 'https://www.youtube.com/lululombard',
                                'logo_fa' : 'youtube'
                            },
                            {
                                'name': 'Reddit',
                                'url' : 'https://www.reddit.com/user/lululombard/',
                                'logo_fa' : 'reddit-alien'
                            },
                        ],
                    },
                    {
                        'name': 'Likyaz',
                        'path_img' : 'http://127.0.0.1:8000/api/v1/skin/head/Likyaz?size=300',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url' : 'https://twitter.com/LikyazRS',
                                'logo_fa' : 'twitter'
                            },
                        ],
                    },
                    {
                        'name': 'Codelta',
                        'path_img' : 'http://127.0.0.1:8000/api/v1/skin/head/Codelta?size=300',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url' : 'https://twitter.com/_Codelta_',
                                'logo_fa' : 'twitter'
                            },
                        ],
                    },
                    {
                        'name': 'Omeganx',
                        'path_img' : 'http://127.0.0.1:8000/api/v1/skin/head/Omeganx?size=300',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url' : 'https://twitter.com/Omeganx',
                                'logo_fa' : 'twitter'
                            },
                        ],
                    },
                    {
                        'name': 'Nano_',
                        'path_img' : 'http://127.0.0.1:8000/api/v1/skin/head/Nano_?size=300',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url' : 'https://twitter.com/Nano1010010110',
                                'logo_fa' : 'twitter'
                            },
                        ],
                    },
                ]
            }
        }


class Vote(BaseViewFrontEnd):
    template_name = 'website/pages/vote.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'vote',
                'websites_list' : [
                    {
                        'titre': 'Serveurs-minecraft.org',
                        'description': 'Liste de serveurs Minecraft JAVA Edition multijoueurs français',
                        'url' : 'https://www.serveurs-minecraft.org/',
                        'path_img' : 'serveurs-minecraft-org.png'
                    },
                    {
                        'titre': 'top-serveurs.net',
                        'description': 'Trouvez facilement un serveur Minecraft sur Top-Serveurs, parmi 2131 serveurs référencés.',
                        'url' : 'https://top-serveurs.net/',
                        'path_img' : 'top-serveurs.png'
                    },
                    {
                        'titre': 'liste-serveur-minecraft.net',
                        'description': 'Bienvenue sur notre liste de serveur minecraft ! Les meilleurs serveurs minecraft sont ici !',
                        'url' : 'http://www.liste-serveur-minecraft.net/',
                        'path_img' : 'liste-serveurs-minecraft.png'
                    },
                    {
                        'titre': 'serveursminecraft.org',
                        'description': 'ServeursMinecraft.org classe ses serveurs minecraft par type de jeu.',
                        'url' : 'https://www.serveursminecraft.org/',
                        'path_img' : 'serveursminecraft-org.png'
                    },
                ]
            }
        }


class Dons(BaseViewFrontEnd):
    template_name = 'website/pages/dons.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'dons'
            }
        }


class Stats(BaseViewFrontEnd):
    template_name = 'website/pages/stats.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'stats'
            }
        }


class Rules(BaseViewFrontEnd):
    template_name = 'website/pages/rules.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'rules'
            }
        }


class Contact(BaseViewFrontEnd):
    template_name = 'website/pages/contact.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'contact'
            }
        }


class Articles(BaseViewFrontEnd):
    template_name = 'website/pages/articles.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'articles'
            }
        }


class Livemap(BaseViewFrontEnd):
    template_name = 'website/pages/livemap.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'livemap'
            }
        }


class About(BaseViewFrontEnd):
    template_name = 'website/pages/about.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'about'
            }
        }


class UrlReducer(View):
    def get(self, request, shortened, *args, **kwargs):
        try:
            query_url = models_api_url_v1.ReducedUrl.objects.get(shortened__exact=shortened)
        except ObjectDoesNotExist:
            return redirect('home')

        return redirect(query_url.url)
