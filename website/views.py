import re

from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import JsonResponse

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

    def post(self, *args, **kwargs):
        post_data = args[0].POST
        
        # get data
        client_type = post_data['client_type']
        minecraft_nickname = post_data['nickname']
        discord_username = post_data['discord_username']
        email = post_data['email']
        message = post_data['message']

        # Clean and valide data
        email, discord_username, message, minecraft_nickname =  self.cleanFormData(email, discord_username, message, minecraft_nickname)
        error_form_data =  self.validateFormData(client_type, email, discord_username, message, minecraft_nickname)

        if error_form_data:
            return JsonResponse({
                'response': 2,
                'error': '\n'.join([err for err in error_form_data])
            })
        
        # compose nickname
        nickname = {
            'player': lambda : ' - '.join([n for n in [minecraft_nickname, discord_username] if n is not '']),
            'other': lambda : f'`{email}`'
        }[client_type]()

        # get ip
        # ip = self.request.headers["cf-connecting-ip"]
        ip = "0.0.0.0"

        # Send message
        discord_service = DiscordService()
        send_error = discord_service.sendContactMessage(nickname, message, ip, client_type)

        if send_error:
            return JsonResponse({'response': 1, 'error': send_error})
        return JsonResponse({'response': 0})
    
    def cleanFormData(self, email, discord_username, message, minecraft_nickname):
        email = email.strip()
        discord_username = discord_username.strip()
        message = message.strip()
        minecraft_nickname = minecraft_nickname.strip()

        return email, discord_username, message, minecraft_nickname

    def validateFormData(self, client_type, email, discord_username, message, minecraft_nickname):
        list_err = []

        client_type_valide = ['player', 'other']
        if not client_type in client_type_valide:
            list_err += ['client_type is not valide']

        min_max_message = (30, 1500)
        if len(message) < min_max_message[0] or len(message) > min_max_message[1]:
            list_err += ['length message is not valide']

        if discord_username:
            valide_discord_username = re.match(r'^.{3,32}#[0-9]{4}$', discord_username)
            if valide_discord_username == None:
                list_err += ['discord username is not valide']

        if email:
            valide_email = re.match(r'^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$', email)
            if valide_email == None:
                list_err += ['email is not valide']

        if minecraft_nickname:
            valide_minecraft_nickname = re.match(r'^[a-zA-Z0-9_]{4,16}$', minecraft_nickname)
            if valide_minecraft_nickname == None:
                list_err += ['minecraft nickname is not valide']

        return list_err


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


class UrlReducer(View):
    def get(self, request, shortened, *args, **kwargs):
        try:
            query_url = models_api_url_v1.ReducedUrl.objects.get(shortened__exact=shortened)
        except ObjectDoesNotExist:
            return redirect('home')

        return redirect(query_url.url)
