from django import forms
from .models import Entrada

class AutoForms(forms.Form):
	nombres = forms.CharField(label='nombres ',max_length=80)
	apellidos = forms.CharField(label='apellidos ',max_length=80)

class EntradaForms(forms.ModelForm):
	class Meta:
		model = Entrada
		exclude =['id_entrada','fecha_hora']