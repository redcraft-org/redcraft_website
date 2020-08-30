from math import *
from django.utils.text import slugify

from api_v1_article import models


class ArticleService:

    def __init__(self, favorit_language=None):
        self.articles = models.Article.objects.all()
        self.favorit_language = favorit_language if favorit_language else models.Language.objects.get(short_name='fr')

    def getLastArticle(self, nb):
        list_article = []
        for article in list(self.articles)[-nb:]:
            article_data = article.articledata_set.get(language=self.favorit_language)
            list_article += [
                {
                    'id': article.id,
                    'title': article_data.title,
                    'overview': article_data.overview,
                    'url': f"/api/v1/articles/{article.id}-{article_data.language.short_name}-{article_data.slug}"
                } 
            ]

        return list_article

    def getList(self, current_page, per_page):
        nb_article = len(self.articles)
        nb_page = ceil(nb_article / per_page)

        if(current_page > nb_page or current_page < 1):
            return {
                'err': 'this page not existe',
                'redirect': f"/api/v1/articles?page={nb_page if current_page > nb_page else 1}&per_page={per_page}"
            }

        next_page = None if current_page >= nb_page else current_page + 1
        prev_page = None if current_page <= 1 else current_page - 1

        list_article = []
        start_article = (current_page - 1) * per_page
        end_article = start_article + per_page
        for article in self.articles[start_article:end_article]:
            article_data = article.articledata_set.get(language=self.favorit_language)
            list_article += [
                {
                    'id': article.id,
                    'title': article_data.title,
                    'overview': article_data.overview,
                    'url': f"/api/v1/articles/{article.id}-{article_data.language.short_name}-{article_data.slug}"
                } 
            ]

        return {
            'nb_page': nb_page,
            'current_page': current_page,
            'next_page': next_page and f"/api/v1/articles?page={next_page}&per_page={per_page}",
            'prev_page': prev_page and f"/api/v1/articles?page={prev_page}&per_page={per_page}",
            'nb_article': nb_article,
            'list': list_article
        }

    def getArticleData(self, id, language):
        try:
            article = models.Article.objects.get(id=id)
            language_object = models.Language.objects.get(short_name=language)
        except models.Article.DoesNotExist:
            return {
                'err': f'{id} not existe'
            }
        except models.Language.DoesNotExist:
            return {
                'err': 'this language is not supported',
                'list_language': [article_data.language.short_name for article_data in article.articledata_set.all()]
            }

        article_data = article.articledata_set.get(language=language_object and self.favorit_language)
        return {
            'id': article_data.article.id,
            'category': article.category.name,
            'path_img': article.path_img,
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

        return {'response': True, 'id': article_object.id}
