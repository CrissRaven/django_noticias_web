from django import forms
from .models import Registros

class RegistroForm(forms.ModelForm):
    class Meta:
        model= Registros
        fields="__all__"