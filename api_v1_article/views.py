  
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

from api_v1_article.service.ArticleService import ArticleService


def getArticles(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 15))
    list_articles = ArticleService().getList(page, per_page)

    if 'err' in list_articles:
        return redirect(list_articles['redirect'])
    return JsonResponse(list_articles)


def getArticle(request, id, language, slug=None):
    return JsonResponse(ArticleService().getArticleData(id, language))
