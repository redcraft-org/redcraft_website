from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from user_agents import parse as parse_user_agents

from api_v1_url import models as models_api_url_v1
from .service.DiscordService import DiscordService
from api_v1_article.service.ArticleService import ArticleService
from network_data.service.NetworkDescriptionService import NetworkDescriptionService
from network_data.service.ServerDescriptionService import ServerDescriptionService


class BaseViewFrontEnd(TemplateView):
    def get_context_data(self, **kwargs):

        user_agent = parse_user_agents(self.request.META['HTTP_USER_AGENT'])
        
        self.network_description_service = NetworkDescriptionService()
        minecraft_versions = self.network_description_service.getMinecraftVersions()
        minecraft_versions_min_max = self.network_description_service.getMinecraftVersionsMinMax()

        return {
            'is_browser_not_supported': 'IE' in str(user_agent),
            'links' : {
                'twitter' : 'https://twitter.com/RedCraftorg',
                'facebook' : 'https://fb.me/RedCraftorg',
                'github' : 'https://github.com/redcraft-org',
                'youtube' : 'https://www.youtube.com/channel/UClo30bzHPYHz847o5WlfE6g',
                'discord' : 'https://discord.gg/h9SfJmh',
                'instagram' : 'https://www.instagram.com/redcraftorg',
            },
            'pages' : [
                {
                    'name' : 'home',
                    'display' : 'Accueil'
                },
                {
                    'name' : 'vote',
                    'display' : 'Vote'
                },
                {
                    'name' : 'dons',
                    'display' : 'Dons'
                },
                {
                    'name' : 'stats',
                    'display' : 'Stats'
                },
                {
                    'name' : 'rules',
                    'display' : 'Règles'
                 },
                {
                    'name' : 'livemap',
                    'display' : 'Live map'
                },
                {
                    'name' : 'contact',
                    'display' : 'Contact'
                }
            ],
            'minecraft_versions' : minecraft_versions,
            'minecraft_versions_min_max' : minecraft_versions_min_max
        }


class Home(BaseViewFrontEnd):
    template_name = 'website/pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()

        discord_service = DiscordService()
        article_service = ArticleService()
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
                
                'network_presentations': self.network_description_service.getAllActive(),
                'servers_list': server_description_service.getAllActive(),
                'staff_list': [
                    {
                        'name': 'lululombard',
                        'path_img' : reverse("get_skin_head", args=["lululombard"]),
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
                        'path_img' : reverse("get_skin_head", args=["Likyaz"]),
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
                        'path_img' : reverse("get_skin_head", args=["Codelta"]),
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
                        'path_img' : reverse("get_skin_head", args=["Omeganx"]),
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
                        'path_img' : reverse("get_skin_head", args=["Nano_"]),
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
                'page': 'vote'
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
