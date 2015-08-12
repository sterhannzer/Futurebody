# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput
from card.models import Card


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = [
            'type',
            'customer',
            'price',
            'date_of_purchase',
            'date_of_finish',
        ]
        labels = {
            'type': 'Typ',
            'customer': 'Klient',
            'price': 'Cena',
            'date_of_purchase': 'Data zakupu',
            'date_of_finish':  'Data wygaśnięcia'
        }
        widgets = {
            'price': TextInput(attrs={'placeholder': 'Cena'})
        }
