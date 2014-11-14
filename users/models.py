from django.db import models
from card.models import Card


class User(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    barcode = models.IntegerField()
    card = models.ForeignKey(Card)


    def __unicode__(self):
        return self.name
