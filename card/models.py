# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime, timedelta
from customers.models import Customer


CHOICES_CARD_TYPE = (
    ('OPEN MESKI (169zl)', 'OPEN MĘSKI (169zł)'),
    ('OPEN_DO_16_M (129zl)', 'OPEN MĘSKI do 16 (129zł)'),
    ('OPEN_RABAT', 'OPEN MĘSKI RABAT'),
    ('STUDENCKI (109zl)', 'STUDENCKI (109zł)'),
    ('SZKOLNY (69zl)', 'SZKOLNY (69zł)'),
    ('OPEN_K (99zl)', 'OPEN KOBIETY (99zł)'),
    ('WEJSCIOWY', 'WEJŚCIOWY'),
)


class Card(models.Model):
    type = models.CharField(max_length=100, choices=CHOICES_CARD_TYPE)
    price = models.IntegerField()
    days = models.CharField(max_length=100, blank=True, null=True)
    customer = models.ForeignKey(Customer)
    date_of_purchase = models.DateField()
    date_of_finish = models.DateField()

    def __unicode__(self):
        return self.type


class CardEntrance(models.Model):
    type = models.CharField(max_length=100, default='Jednorazowy', editable=False)
    price = models.IntegerField()
    customer = models.ForeignKey(Customer)
    date_of_purchase = models.DateField()
    number_entry = models.IntegerField()

    def __unicode__(self):
        return self.type
