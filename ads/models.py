from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    address = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=100)
