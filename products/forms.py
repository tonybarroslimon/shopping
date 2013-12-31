from django import forms
from django.forms import ChoiceField
from django.forms.extras import widgets

QUANTITIES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)    
)

class ProductAdd(forms.Form):
    quantity = forms.ChoiceField(widget=forms.Select, choices=QUANTITIES)
    #code
