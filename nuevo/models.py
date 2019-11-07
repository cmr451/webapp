from django.db import models

# Create your models here.
class cliente(models.Model):
	id_c = models.AutoField(primary_key = True)
	dni = models.CharField(max_length =50)
	nombre = models.CharField(max_length =50)
	direccion = models.CharField(max_length =50)
	def __str__(self):
		return self.nombres+' '+self.apellidos

class publicacion(models.Model):
	id_s = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length =50)
	tema = models.CharField(max_length =50)
	descripcion = models.CharField(max_length =50)
	

class numero(models.Model):
	fecha = models.CharField(max_length =50)
	resumen = models.TextField()

