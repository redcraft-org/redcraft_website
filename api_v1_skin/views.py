from django.http import HttpResponse, JsonResponse

from api_v1_skin.service.SkinService import SkinService


def getTemplateSkin(request, ref):
    skin = SkinService(ref)
    err = skin.loadRequest(request)
    if err: return JsonResponse({'err': err})
    return HttpResponse(skin.renderTemplate(), content_type="image/png")

def getHeadSkin(request, ref):
    skin = SkinService(ref)
    err = skin.loadRequest(request)
    if err: return JsonResponse({'err': err})
    return HttpResponse(skin.renderHead(), content_type="image/png")

def getBodySkin(request, ref):
    skin = SkinService(ref)
    err = skin.loadRequest(request)
    if err: return JsonResponse({'err': err})
    return HttpResponse(skin.renderBody(), content_type="image/png")
