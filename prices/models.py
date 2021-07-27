from django.db import models

class item(models.Model):
    item = models.CharField(max_length=200)

class price(models.Model):
    price = models.FloatField()
    discount = models.FloatField()


class objects(models.Model):
    item = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()

