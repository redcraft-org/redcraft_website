from django.contrib import admin

from .models import Token, ReducedUrl


admin.site.register(ReducedUrl)
admin.site.register(Token)
