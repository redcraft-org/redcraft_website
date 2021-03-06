import json
import random
import string
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from api_v1_url import models


class GetUrlList(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                e.shortened: {
                    'token': e.token.acces_name,
                    'url': e.url,
                } for e in models.ReducedUrl.objects.all()
            }
        )


class SetUrl(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SetUrl, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        json_body = json.loads(request.body)

        try:
            token = models.Token.objects.get(token=json_body['token'])
            url = models.ReducedUrl.objects.get(url=json_body['url'])
        except models.Token.DoesNotExist:
            return JsonResponse({'err': "token don't existe"})
        except models.ReducedUrl.DoesNotExist:
            url = None
        else:
            return JsonResponse({
                'err': "url existe", 
                'shortened': url.shortened
            })

        shortened = json_body['shortened'] or ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        url = models.ReducedUrl(token=token, url=json_body['url'], shortened=shortened)
        url.save()
        return JsonResponse({'response': True})
