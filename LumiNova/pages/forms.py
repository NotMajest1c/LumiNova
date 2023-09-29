from django import forms
from .models import *
from django.core.exceptions import ValidationError
class Productform(forms.ModelForm):
    class Meta:
        model = product
        fields = [
            'title',
            'description',
            'price',
        ]

