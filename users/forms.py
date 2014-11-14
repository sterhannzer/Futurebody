from django.forms import ModelForm, TextInput
from users.models import User


class UserForm(ModelForm):
    class Meta:
        model = User

        fields = [
            'name',
            'surname',
            'barcode',
            'card'
        ]

