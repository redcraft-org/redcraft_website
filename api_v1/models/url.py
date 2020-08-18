from django.db import models


class ReducedUrl(models.Model):
    token = models.ForeignKey(
        'Token',
        on_delete=models.CASCADE,
    )
    url = models.CharField(max_length=2048)
    shortened = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.shortened} - {self.token.acces_name}"
