from django.db import models



class usuario(models.Model):
	#extiendo el modelo de usuario de django
	nombre = models.EmailField(max_length=100)	
	correo = models.EmailField(max_length=100)
	telefono = models.CharField(max_length=15)
	pais = models.CharField(max_length=30)

	

	def __str__(self):
		return self.user.username

class informacion(models.Model):

	nombre = models.CharField(max_length=100)
	correo = models.EmailField(max_length=150)
	telefono = models.CharField(max_length=50)
	pais = models.CharField(max_length=30)


	def __str__(self):
		return self.nombre