# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, timedelta

CHOICES_TYPE = (
    ('OPEN MESKI (169zl)', 'OPEN MĘSKI (169zł)'),
    ('OPEN_DO_16_M (129zl)', 'OPEN MĘSKI do 16 (129zł)'),
    ('OPEN_RABAT', 'OPEN MĘSKI RABAT'),
    ('STUDENCKI (109zl)', 'STUDENCKI (109zł)'),
    ('SZKOLNY (69zl)', 'SZKOLNY (69zł)'),
    ('OPEN_K (99zl)', 'OPEN KOBIETY (99zł)'),
    ('WEJSCIOWY', 'WEJŚCIOWY'),

)

class Card(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=100, choices=CHOICES_TYPE)
    price = models.IntegerField()
    date_of_purchase = models.DateField(default=datetime.now())
    date_of_finish = models.DateField(default=datetime.now()+timedelta(days=30))

    def __unicode__(self):
        return self.name
