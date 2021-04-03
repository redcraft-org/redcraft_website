from math import *
from django.utils.text import slugify

from api_v1_article import models


class ArticleService:

    def __init__(self, favorite_language=None):
        self.articles = models.Article.objects.all()
        self.favorite_language = favorite_language if favorite_language else models.Language.objects.get(short_name='fr')

    def getLastArticle(self, nb):
        list_article = []
        for article in list(self.articles)[-nb:]:
            article_data = article.articledata_set.get(language=self.favorite_language)
            list_article += [
                {
                    'id': article.id,
                    'title': article_data.title,
                    'overview': article_data.overview,
                    'url': f"/article/{article_data.language.short_name}/{article.id}-{article_data.slug}.html"
                }
            ]

        return list_article

    def getList(self, current_page, per_page):
        nb_article = len(self.articles)
        nb_page = ceil(nb_article / per_page)

        next_page = None if current_page >= nb_page else current_page + 1
        prev_page = None if current_page <= 1 else current_page - 1

        start_article = (current_page - 1) * per_page
        end_article = start_article + per_page

        list_article = []
        for article in self.articles[start_article:end_article]:
            article_data = article.articledata_set.get(language=self.favorite_language)
            list_article += [
                {
                    'id': article.id,
                    'title': article_data.title,
                    'overview': article_data.overview,
                    'short_name': article_data.language.short_name,
                    'slug': article_data.slug,
                    'path_img': article.path_img,
                }
            ]

        return {
            'nb_page': nb_page,
            'current_page': current_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'nb_article': nb_article,
            'list': list_article,
            'per_page': per_page,
        }

    def getArticleData(self, id, language=None):
        article = models.Article.objects.get(id=id)
        try:
            language_object = language and models.Language.objects.get(short_name=language)
        except models.Language.DoesNotExist:
            return {
                'err': f'the language `{language}` is not supported',
                'list_language': [article_data.language.short_name for article_data in article.articledata_set.all()]
            }

        article_data = article.articledata_set.get(language=language_object and self.favorite_language)
        return {
            'id': article_data.article.id,
            'title': article_data.title,
            'text': article_data.text,
            'overview': article_data.overview,
            'slug': article_data.slug,
            'language': article_data.language.name,
        }

    def createArticle(self, path_img, category_name, articles_data):
        try:
            category_object = models.Category.objects.get(name=category_name)
        except models.Category.DoesNotExist:
            return {'err': f'{category_name} not existe'}

        for article_data in articles_data:
            try:
                language_object = models.Language.objects.get(short_name=article_data['language'])
            except models.Language.DoesNotExist:
                return {'err': f"{article_data['language']} language is not supported"}
            else:
                article_data['language_object'] = language_object

        article_object = models.Article(path_img=path_img, category=category_object)
        article_object.save()

        for article_data in articles_data:
            slug = slugify(article_data['slug'] if 'slug' in article_data else article_data['title'])
            overview = article_data['overview'] if 'overview' in article_data else f"{article_data['text'][:60]} ..."

            article_data_object = models.ArticleData(
                title=article_data['title'],
                text=article_data['text'],
                language=article_data['language_object'],
                overview=overview,
                slug=slug,
                article=article_object
            )
            article_data_object.save()

        return {'response': True}
