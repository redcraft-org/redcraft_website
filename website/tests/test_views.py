from django.test import TestCase, Client

# from website import views


class FrontviewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def assertBaseContext(self, response):
        self.assertEqual(response.context['links'], {
            'twitter' : 'https://twitter.com/RedCraftorg',
            'facebook' : 'https://fb.me/RedCraftorg',
            'github' : 'https://github.com/redcraft-org',
            'youtube' : 'https://www.youtube.com/channel/UClo30bzHPYHz847o5WlfE6g',
            'discord' : 'https://discord.gg/h9SfJmh',
            'instagram' : 'https://www.instagram.com/redcraftorg',
        })

    def test_succes_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('website/pages/home.html')
        self.assertBaseContext(response)
        self.assertEqual(response.context['page'], 'home')
        

    def test_succes_vote(self):
        response = self.client.get('/vote.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('website/pages/vote.html')
        self.assertBaseContext(response)
        self.assertEqual(response.context['page'], 'vote')
        
    def test_succes_donnations(self):
        response = self.client.get('/dons.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('website/pages/dons.html')
        self.assertBaseContext(response)
        self.assertEqual(response.context['page'], 'dons')
        
    def test_succes_status(self):
        response = self.client.get('/stats.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('website/pages/stats.html')
        self.assertBaseContext(response)
        self.assertEqual(response.context['page'], 'stats')
        
    def test_succes_rules(self):
        response = self.client.get('/rules.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('website/pages/rules.html')
        self.assertBaseContext(response)
        self.assertEqual(response.context['page'], 'rules')
        
    def test_succes_articles(self):
        response = self.client.get('/articles.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('website/pages/articles.html')
        self.assertBaseContext(response)
        self.assertEqual(response.context['page'], 'articles')
        
    def test_succes_articles(self):
        response = self.client.get('/dynmap.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('website/pages/dynmap.html')
        self.assertBaseContext(response)
        self.assertEqual(response.context['page'], 'dynmap')
