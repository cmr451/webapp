from django import forms

class AutoForms(forms.Form):
	dni = forms.CharField(label='dni ',max_length=80)
	nombre = forms.CharField(label='nombre',max_length=80)
	direccion = forms.CharField(label='direccion',max_length=80)