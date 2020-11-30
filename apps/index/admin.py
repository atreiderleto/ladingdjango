from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from apps.index.models import informacion



@admin.register(informacion)

class adminRegistro(admin.ModelAdmin):
	list_display = ('pk', 'nombre', 'correo', 'telefono', 'pais')