from django.test import TestCase
from api_v1_article.service import ArticleService
from api_v1_article import models


class ArticleServiceCreateTestCase(TestCase):
    fixtures = ['category.json', 'language.json','article.json']

    def setUp(self):
        # Set article
        self.article_1 = models.Article.objects.get(id=1)
        self.article_data_fr = models.ArticleData.objects.get(id=1)
        self.article_data_en = models.ArticleData.objects.get(id=2)

        article_service = ArticleService()

    def test_succes_create_full(self):
        res = ArticleService().createArticle(
            path_img='path_img_article_1',
            category_name='redstone',
            articles_data=[
                {
                    'title': 'Un titre de redstone',
                    'text': 'Un article de redstone',
                    'slug': 'un-slug-redstone',
                    'overview': 'Un overview de redstone',
                    'language':'fr'
                }
            ]
        )

        article = models.Article.objects.get(id=res['id'])
        category_redstone = models.Category.objects.get(name='redstone')
        language_fr = models.Language.objects.get(short_name='fr')

        self.assertEqual(article.category, category_redstone)

        article_data = article.articledata_set.get(language=language_fr)

        self.assertEqual(article_data.title, 'Un titre de redstone')
        self.assertEqual(article_data.text, 'Un article de redstone')
        self.assertEqual(article_data.slug, 'un-slug-redstone')
        self.assertEqual(article_data.overview, 'Un overview de redstone')
        self.assertEqual(article_data.language, language_fr)

    def test_succes_create_without_optional_params(self):
        res = ArticleService().createArticle(
            path_img='path_img_article_1',
            category_name='redstone',
            articles_data=[
                {
                    'title': 'Un titre de redstone',
                    'text': 'Un article de redstone: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis nulla at tellus bibendum, nec luctus proin.',
                    'language':'fr'
                }
            ]
        )

        article = models.Article.objects.get(id=res['id'])
        category_redstone = models.Category.objects.get(name='redstone')
        language_fr = models.Language.objects.get(short_name='fr')

        self.assertEqual(article.category, category_redstone)

        article_data = article.articledata_set.get(language=language_fr)

        self.assertEqual(article_data.title, 'Un titre de redstone')
        self.assertEqual(article_data.text, 'Un article de redstone: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis nulla at tellus bibendum, nec luctus proin.')
        self.assertEqual(article_data.slug, 'un-titre-de-redstone')
        self.assertEqual(article_data.overview, 'Un article de redstone: Lorem ipsum dolor sit amet, consecte ...')
        self.assertEqual(article_data.language, language_fr)

    def test_failure_create_bad_language(self):
        res = ArticleService().createArticle(
            path_img='path_img_article_1',
            category_name='redstone',
            articles_data=[
                {
                    'title': 'Un titre de redstone',
                    'text': 'Un article de redstone',
                    'language':'frr'
                }
            ]
        )

        self.assertEqual(res['err'], 'frr language is not supported')

    def test_failure_create_bad_category(self):
        res = ArticleService().createArticle(
            path_img='path_img_article_1',
            category_name='redstonee',
            articles_data=[
                {
                    'title': 'Un titre de redstone',
                    'text': 'Un article de redstone',
                    'language':'fr'
                }
            ]
        )

        self.assertEqual(res['err'], 'redstonee not existe')

    def test_succes_get_article_data(self):
        article = ArticleService().getArticleData(id=self.article_1.id, language='fr')

        self.assertEqual(article['id'], self.article_1.id)
        self.assertEqual(article['category'], self.article_1.category.name)
        self.assertEqual(article['path_img'], self.article_1.path_img)
        
        self.assertEqual(article['title'], self.article_data_fr.title)
        self.assertEqual(article['text'], self.article_data_fr.text)
        self.assertEqual(article['overview'], self.article_data_fr.overview)
        self.assertEqual(article['slug'], self.article_data_fr.slug)
        self.assertEqual(article['language'], self.article_data_fr.language.name)

    def test_failure_get_article_data_bad_id(self):
        res = ArticleService().getArticleData(id=5555, language='fr')
        self.assertEqual(res['err'], '5555 not existe')

    def test_failure_get_article_data_bad_language(self):
        res = ArticleService().getArticleData(id=self.article_1.id, language='frr')

        self.assertEqual(res['err'], 'this language is not supported')
        self.assertEqual(res['list_language'], ['fr', 'en'])

    def test_succes_get_list(self):
        res = ArticleService().getList(2, 5)
        
        articles = list(models.Article.objects.all())
        language_fr = models.Language.objects.get(short_name='fr')

        self.assertEqual(res['nb_page'], 4)
        self.assertEqual(res['current_page'], 2)
        self.assertEqual(res['next_page'], '/api/v1/articles?page=3&per_page=5')
        self.assertEqual(res['prev_page'], '/api/v1/articles?page=1&per_page=5')
        self.assertEqual(res['nb_article'], len(articles))
        self.assertEqual(res['list'], [
                {
                    'id': article.id,
                    'title': article.articledata_set.get(language=language_fr).title,
                    'overview': article.articledata_set.get(language=language_fr).overview,
                    'url': f"/api/v1/articles/{article.id}-{article.articledata_set.get(language=language_fr).language.short_name}-{article.articledata_set.get(language=language_fr).slug}",
                } for article in articles[5:10]
            ])

    def test_succes_get_list(self):
        res = ArticleService().getList(2, 5)

        articles = list(models.Article.objects.all())
        language_fr = models.Language.objects.get(short_name='fr')

        self.assertEqual(res['nb_page'], 4)
        self.assertEqual(res['current_page'], 2)
        self.assertEqual(res['next_page'], '/api/v1/articles?page=3&per_page=5')
        self.assertEqual(res['prev_page'], '/api/v1/articles?page=1&per_page=5')
        self.assertEqual(res['nb_article'], len(articles))
        self.assertEqual(res['list'], 
            [
                {
                    'id': article.id,
                    'title': article.articledata_set.get(language=language_fr).title,
                    'overview': article.articledata_set.get(language=language_fr).overview,
                    'url': f"/api/v1/articles/{article.id}-{article.articledata_set.get(language=language_fr).language.short_name}-{article.articledata_set.get(language=language_fr).slug}",
                } for article in articles[5:10]
            ]
        )

    def test_failure_get_list_current_page_bigger(self):
        res = ArticleService().getList(10, 5)
        
        self.assertEqual(res['err'], 'this page not existe')
        self.assertEqual(res['redirect'], '/api/v1/articles?page=4&per_page=5')


    def test_failure_get_list_current_page_smaller(self):
        res = ArticleService().getList(0, 5)
        
        self.assertEqual(res['err'], 'this page not existe')
        self.assertEqual(res['redirect'], '/api/v1/articles?page=1&per_page=5')

    def test_succes_get_last_articles(self):
        res = ArticleService().getLastArticle(3)

        articles = list(models.Article.objects.all())
        language_fr = models.Language.objects.get(short_name='fr')

        self.assertEqual(res, 
            [
                {
                    'id': article.id,
                    'title': article.articledata_set.get(language=language_fr).title,
                    'overview': article.articledata_set.get(language=language_fr).overview,
                    'url': f"/api/v1/articles/{article.id}-{article.articledata_set.get(language=language_fr).language.short_name}-{article.articledata_set.get(language=language_fr).slug}",
                } for article in articles[-3:]
            ]
        )


