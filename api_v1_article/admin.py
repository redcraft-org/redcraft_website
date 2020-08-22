from django.contrib import admin

from api_v1_article import models


admin.site.register(models.Language)
admin.site.register(models.Category)
admin.site.register(models.ArticleData)
admin.site.register(models.Article)
