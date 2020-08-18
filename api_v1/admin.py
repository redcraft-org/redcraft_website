from django.contrib import admin

from .models.url import ReducedUrl
from .models.common import Token


admin.site.register(ReducedUrl)
admin.site.register(Token)