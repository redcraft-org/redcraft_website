from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    grade = models.CharField(max_length=20)