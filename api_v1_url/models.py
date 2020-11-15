from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=32)
    access_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.access_name} - {self.token}"


class ReducedUrl(models.Model):
    token = models.ForeignKey(
        'Token',
        on_delete=models.CASCADE,
    )
    url = models.CharField(max_length=2048)
    shortened = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.shortened} - {self.token.access_name}"
