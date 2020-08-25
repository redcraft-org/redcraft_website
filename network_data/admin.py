from django.contrib import admin

from network_data import models


admin.site.register(models.ServerDescription)
admin.site.register(models.NetworkDescription)
