import json
from django.test import TestCase, Client

from api_v1_url import models


class UrlViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.token = models.Token.objects.create(token='test-token', acces_name='test-acces')
        self.reduce_url_1 = models.ReducedUrl.objects.create(
            token=self.token,
            url='https://github.com',
            shortened='github'
        )

    def test_succes_get_url_list(self):
        response = self.client.get('/api/v1/urls')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            self.reduce_url_1.shortened: {
                'token': self.reduce_url_1.token.acces_name,
                'url': self.reduce_url_1.url
            }
        })

    def test_succes_set_url_create_shortened(self):
        response = self.client.post('/api/v1/url', {
            'token': 'test-token',
            'url': 'https://github.com/redcraft-org',
            'shortened': 'rc-github',
        }, content_type='application/json')
        reduce_url = models.ReducedUrl.objects.get(shortened='rc-github')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'response': True, 'shortened': 'rc-github'})
        self.assertEqual(reduce_url.token, self.token)
        self.assertEqual(reduce_url.url, 'https://github.com/redcraft-org')
        self.assertEqual(reduce_url.shortened, 'rc-github')

    def test_succes_set_url_create_without_shortened(self):
        response = self.client.post('/api/v1/url', {
            'token': 'test-token',
            'url': 'https://github.com/redcraft-org/redcraft_website',
        }, content_type='application/json')
        content = json.loads(response.content)
        reduce_url = models.ReducedUrl.objects.get(shortened=content['shortened'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(reduce_url.token, self.token)
        self.assertEqual(reduce_url.url, 'https://github.com/redcraft-org/redcraft_website')
        self.assertEqual(reduce_url.shortened, content['shortened'])
