from django.db import models



class informacion(models.Model):
	#modelo de formularip para informacion 
	nombre = models.CharField(max_length=100)
	correo = models.EmailField(max_length=150)
	telefono = models.CharField(max_length=50)
	pais = models.CharField(max_length=30)


	def __str__(self):
		return self.nombre