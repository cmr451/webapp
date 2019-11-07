from django.db import models

class registro(models.Model):
	numero = models.IntegerField()
	nombre = models.CharField(max_length = 120)
	
		