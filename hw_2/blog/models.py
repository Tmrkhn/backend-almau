from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=2000)
    author = models.CharField(max_length=255)
