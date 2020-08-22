from math import *
from api_v1_article import models


class ArticleService:

    def __init__(self, favorit_language=None):
        self.articles = models.Article.objects.all()
        self.favorit_language = favorit_language if favorit_language else models.Language.objects.get(short_name='fr')

    def getList(self, current_page, per_page):
        nb_article = len(self.articles)
        nb_page = ceil(nb_article / per_page)

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

        print(next_page)
        print(prev_page)
        return {
            'nb_page': nb_page,
            'current_page': current_page,
            'next_page': next_page and f"/api/v1/articles?page={next_page}&per_page={per_page}",
            'prev_page': prev_page and f"/api/v1/articles?page={prev_page}&per_page={per_page}",
            'nb_article': nb_article,
            'list': list_article
        }

    def getArticleData(self, id, language=None):
        article = models.Article.objects.get(id=id)
        try:
            language_object = language and models.Language.objects.get(short_name=language)
        except models.Language.DoesNotExist:
            return {
                'err': 'this language is not supported',
                'list_language': [article_data.language.short_name for article_data in article.articledata_set.all()]
            }

        article_data = article.articledata_set.get(language=language_object and self.favorit_language)
        return {
            'id': article_data.article.id,
            'title': article_data.title,
            'text': article_data.text,
            'overview': article_data.overview,
            'slug': article_data.slug,
            'language': article_data.language.name,
        }
