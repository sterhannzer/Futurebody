# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput
from card.models import Card, CardEntrance



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
            'type': 'Karnet',
            'customer': 'Klient',
            'price': '',
            'date_of_purchase': 'Data zakupu',
            'date_of_finish':  'Data ważności',

        }
        widgets = {
            'price': TextInput(attrs={'placeholder': 'Cena'})
        }


class CardEntranceForm(ModelForm):
    class Meta:
        model = CardEntrance
        fields = [
            'customer',
            'price',
            'date_of_purchase',
            'number_entry',

        ]
        labels = {
            'customer': 'Klient',
            'price': '',
            'date_of_purchase': 'Data zakupu',
            'number_entry': ''
        }
        widgets = {
            'price': TextInput(attrs={'placeholder': 'Cena'}),
        }
