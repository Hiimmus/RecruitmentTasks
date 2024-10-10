from django import forms
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError


class PeselForm(forms.Form):
    number = forms.CharField(
        label='Numer PESEL',
        max_length=11,
        min_length=11,
        required=True,
        validators=[
            MinLengthValidator(11),
        ]
    )
