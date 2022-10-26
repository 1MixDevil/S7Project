from django.forms import ModelForm
from django import forms
from .models import Yarik
from S7Project.settings import FIELDS_CONST, CHOICE_CONST

class StartForm(ModelForm):
    class Meta:
        model = Yarik
        fields = FIELDS_CONST
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) for field in list(set(fields) - set(CHOICE_CONST))
        }
        for i in CHOICE_CONST:
            widgets[i] = forms.Select(attrs={'class': 'form-control'})
