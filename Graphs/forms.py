from django.forms import ModelForm
from django import forms
from .models import Yarik
from S7Project.settings import FIELDS_CONST
Choise_Form = ["engine_type", "flight_phase", "aircraft_grp", "engine_family", "manufacturer", "aircraft_family", "aircraft_type", "ac_manufacturer"]

class StartForm(ModelForm):
    class Meta:
        model = Yarik
        fields = FIELDS_CONST
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) for field in list(set(fields) - set(Choise_Form))
        }
        for i in Choise_Form:
            widgets[i] = forms.Select(attrs={'class': 'form-control'})
