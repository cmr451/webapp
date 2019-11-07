from django import form


class registroForm(form.Form):
	numero = form.IntegerField()
	nombres = form.CharField(label='nombre',max_length=80)