from django.shortcuts import render
from .models import AutoForms

def cliente(request):
		form = AutoForms
		todosCliente=cliente.objects.all()
		return render(request,'cliente.html',{'cliente':todosCliente, 'form':form})

def publicacion(request):
	pass