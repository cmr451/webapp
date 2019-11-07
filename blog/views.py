from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Autor
from .models import Entrada
from .forms import AutoForms
from .forms import *


"""def welcome(request):
	return HttpResponse('<center><h1>Welcome to this Site</h1></center>')"""
def welcome(request):
	return render(request,'welcome.html')
def autores(request):
	if request.method == 'POST':
		form = AutoForms(request.POST)
		if form.is_valid():
			autor = Autor()
			autor.nombres = form.cleaned_data['nombres']
			autor.apellidos = form.cleaned_data['apellidos']
			autor.save()
			return redirect('autores')
	else :
		form = AutoForms
		todosAutores=Autor.objects.all()
		return render(request,'autores.html',{'autores':todosAutores, 'form':form})

def entradas(request):
	if request.method == 'POST':
		form2 = EntradaForms(request.POST)
		if form2.is_valid():
			entrada = Entrada()
			entrada.titular = form2.cleaned_data['titular']
			entrada.contenido = form2.cleaned_data['contenido']
			entrada.autor = form2.cleaned_data['autor']
			entrada.save()
			return redirect('entradas')
	else:
		form2 = EntradaForms
		todosEntradas=Entrada.objects.all()
		return render(request,'entradas.html',{'entradas':todosEntradas, 'form2':form2})


