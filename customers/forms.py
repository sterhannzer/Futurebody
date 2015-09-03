# coding=utf-8
from django.forms import ModelForm, TextInput, Textarea
from customers.models import Customer


class UserForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name',
            'surname',
            'barcode',
        ]
        labels = {
            'name': '',
            'surname': '',
            'barcode': ''
        }
        widgets = {
        'name': TextInput(attrs={'label': "", 'placeholder': 'Imię klienta', 'class': ''}),
        'surname': TextInput(attrs={'placeholder': 'Nazwisko klienta'}),
        'barcode': TextInput(attrs={'placeholder': 'Kod kreskowy'})
        }