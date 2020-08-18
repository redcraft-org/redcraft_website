from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=32)
    acces_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.acces_name} - {self.token}"
