# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput
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
        labels = {
            'name': 'Nazwa',
            'type': 'Typ',
            'price': 'Cena',
            'date_of_purchase': 'Data zakupu',
            'date_of_finish':  'Data wygaśnięcia'
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Nazwa'}),
            'price': TextInput(attrs={'placeholder': 'Cena'})
        }
