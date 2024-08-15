from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class selects_cupo(forms.Form):
    day=forms.ModelChoiceField(queryset=Dia.objects.all(),label="Selecione dia:",widget=forms.Select)
    type = forms.ModelChoiceField(queryset=Tipo_Menu.objects.all(), label="Tipo:")  # Usar queryset con instancias de Tipo_Menu
    
class iniciar_sesion(AuthenticationForm):
    codigo_u=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))