from django.forms import ModelForm
from django import forms
from .models import Yarik
from S7Project.settings import FIELDS_CONST


class StartForm(ModelForm):
    class Meta:
        model = Yarik
        fields = FIELDS_CONST
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) for field in fields
        }
