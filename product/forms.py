from django import forms
from product.models import *


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=350, required=True, widget=forms.Textarea)
    price = forms.FloatField(min_value=0, max_value=1000000)
    in_stock = forms.BooleanField(required=True)
