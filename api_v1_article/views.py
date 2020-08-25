  
from django.http import HttpResponse, JsonResponse

from api_v1_article.service.ArticleService import ArticleService


def getArticles(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 15))
    return JsonResponse(ArticleService().getList(page, per_page))


def getArticle(request, id, language, slug=None):
    return JsonResponse(ArticleService().getArticleData(id, language))
