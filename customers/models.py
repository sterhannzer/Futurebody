from django.db import models
from card.models import Card


class Customer(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    barcode = models.IntegerField()

    def __unicode__(self):
        return self.name
