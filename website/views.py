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
                'server_presentations': [
                    {
                        'title': 'Un serveur unique.',
                        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eget feugiat lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quis leo a felis cursus pharetra id vitae felis.',
                        'img': 'dynmap.png',
                    },
                    {
                        'title': 'Un staff compétent.',
                        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eget feugiat lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quis leo a felis.',
                        'img': 'home-background-2.png',
                    },
                    {
                        'title': 'Rejoignez-nous.',
                        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eget feugiat lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quis leo.',
                        'img': 'home-background.png',
                    },
                ],
                'servers_list': [
                    {
                        'title': 'Créatif Build',
                        'overview' : 'Aenean rutrum erat at neque auctor varius. Sed pellentesque tortor purus, non ultrices sem vehicula ut. Donec vel enim arcu.',
                        'description' : 'Praesent ac urna enim. Nunc sodales justo accumsan consectetur ornare. Ut laoreet in eros id ullamcorper. Integer sit amet diam vel lorem placerat ultricies sed sit amet odio. Donec nulla lectus, rutrum non dui eu, varius imperdiet mi.',
                        'img' : 'dynmap.png',
                    },
                    {
                        'title': 'Créatif Redstone',
                        'overview' : 'Quisque sodales ante et diam tempor, id consectetur nibh scelerisque. Cras quis ex id nisi scelerisque vestibulum.',
                        'description' : 'Praesent ac urna enim. Nunc sodales justo accumsan consectetur ornare. Ut laoreet in eros id ullamcorper. Integer sit amet diam vel lorem placerat ultricies sed sit amet odio. Donec nulla lectus, rutrum non dui eu, varius imperdiet mi.',
                        'img' : 'dynmap.png',
                    },
                    {
                        'title': 'Survie',
                        'overview' : 'Quisque ut orci semper, ullamcorper quam a, interdum turpis. Curabitur est nisl, rhoncus ac sapien quis, tempor eleifend turpis.',
                        'description' : 'Praesent ac urna enim. Nunc sodales justo accumsan consectetur ornare. Ut laoreet in eros id ullamcorper. Integer sit amet diam vel lorem placerat ultricies sed sit amet odio. Donec nulla lectus, rutrum non dui eu, varius imperdiet mi.',
                        'img' : 'dynmap.png',
                    },
                    {
                        'title': 'Factions',
                        'overview' : 'Curabitur lobortis hendrerit leo, a porta tellus porta eu. Ut scelerisque nisi auctor iaculis pretium.',
                        'description' : 'Praesent ac urna enim. Nunc sodales justo accumsan consectetur ornare. Ut laoreet in eros id ullamcorper. Integer sit amet diam vel lorem placerat ultricies sed sit amet odio. Donec nulla lectus, rutrum non dui eu, varius imperdiet mi.',
                        'img' : 'dynmap.png',
                    },
                ],
                'staff_list': {

                }
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


class Dynmap(BaseViewFrontEnd):
    template_name = 'website/pages/dynmap.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        
        return {
            **ctx,
            **{
                'page': 'dynmap'
            }
        }


class UrlReducer(View):
    def get(self, request, shortened, *args, **kwargs):
        try:
            query_url = models_api_v1.ReducedUrl.objects.get(shortened__exact=shortened)
        except ObjectDoesNotExist:
            return redirect('home')

        return redirect(query_url.url)
