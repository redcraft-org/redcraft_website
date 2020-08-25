from django.db import models


class ServerDescription(models.Model):
    title = models.CharField(max_length=42)
    text = models.CharField(max_length=280)
    overview = models.CharField(max_length=64)
    path_img = models.CharField(max_length=128)
    active = models.BooleanField()

    def __str__(self):
        return f"{self.title}"


class NetworkDescription(models.Model):
    title = models.CharField(max_length=42)
    overview = models.CharField(max_length=64)
    text = models.CharField(max_length=280)
    path_img = models.CharField(max_length=128)
    active = models.BooleanField()

    def __str__(self):
        return f"{self.title}"
