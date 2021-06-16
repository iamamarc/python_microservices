from django.db import models

# Create your models here.


class Product(models.Model):
    # id field will be present
    # no need to specify this

    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    # id field will be present
    # no need to specify this

    pass

