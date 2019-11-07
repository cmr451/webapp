from django.shortcuts import render


def index(request):
	return render(request,'inicio.html',{'range':range(1,670)})

def registro(request):
	registros = registro.objects.all()
	return render(request,'registro.html')

def faltantes(request):
	return render(request, 'faltantes.html')

