from django.db import models


class Language(models.Model):
    short_name = models.CharField(max_length=4)
    name = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.short_name} - {self.name}"


class ArticleData(models.Model):
    title = models.CharField(max_length=42)
    text = models.CharField(max_length=280) # Limit by twitter
    overview = models.CharField(max_length=64, blank=True, null=True)
    slug = models.CharField(max_length=42, blank=True, null=True)
    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title} - {self.overview}"


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
