from django.test import TestCase, Client

from api_v1_article import models

class ArticleViewsTestCase(TestCase):
    fixtures = ['category.json', 'language.json', 'articles.json']

    def setUp(self):
        self.client = Client()

        self.article_1 = models.Article.objects.get(id=1)
        self.article_data_fr = models.ArticleData.objects.get(id=1)

    def test_succes_get_articles(self):
        response = self.client.get('/api/v1/articles/')

        articles = list(models.Article.objects.all())
        language_fr = models.Language.objects.get(short_name='fr')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            'nb_page': 2,
            'current_page': 1,
            'next_page': '/api/v1/articles?page=2&per_page=15',
            'prev_page': None,
            'nb_article': len(articles),
            'list': [
                {
                    'id': article.id,
                    'title': article.articledata_set.get(language=language_fr).title,
                    'overview': article.articledata_set.get(language=language_fr).overview,
                    'url': f"/api/v1/articles/{article.id}-{article.articledata_set.get(language=language_fr).language.short_name}-{article.articledata_set.get(language=language_fr).slug}",
                } for article in articles[0:15]
            ]
        })

    def test_succes_get_articles_page_bigger(self):
        response = self.client.get('/api/v1/articles/', {'page': 100}, follow=True)
        self.assertRedirects(response, '/api/v1/articles/?page=2&per_page=15')

    def test_succes_get_articles_page_smaller(self):
        response = self.client.get('/api/v1/articles/', {'page': -1}, follow=True)
        self.assertRedirects(response, '/api/v1/articles/?page=1&per_page=15')

    def test_succes_get_article(self):
        article = models.Article.objects.get(id=1)
        article_data = models.ArticleData.objects.get(id=1)
        response = self.client.get('/api/v1/articles/1-fr-un-slug-build')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            'id': article_data.article.id,
            'category': article.category.name,
            'path_img': article.path_img,
            'title': article_data.title,
            'text': article_data.text,
            'overview': article_data.overview,
            'slug': article_data.slug,
            'language': article_data.language.name,
        })

    def test_succes_get_article_whit_bad_slug(self):
        response = self.client.get('/api/v1/articles/1-fr-bad-slug')
        self.assertEqual(response.status_code, 200)

    def test_succes_get_article_whitout_slug(self):
        response = self.client.get('/api/v1/articles/1-fr')
        self.assertEqual(response.status_code, 200)
