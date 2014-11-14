# -*- coding: utf-8 -*-
from django.forms import ModelForm
from card.models import Card


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = [
            'name',
            'type',
            'price',
            'date_of_purchase',
            'date_of_finish',
        ]
