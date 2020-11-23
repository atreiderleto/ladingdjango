from django.db import models

from django.contrib.auth.models import User


class usuario(models.Model):
	#extiendo el modelo de usuario de django 
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	#campos nuevo de la tabla usuario	
	correo = models.EmailField(max_length=100)
	telefono = models.CharField(max_length=15)
	pais = models.CharField(max_length=30)

	

	def __str__(self):
		return self.user.username


