from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#modelo usuario

from apps.index.models import informacion



def landingPage(request):
	return render(request, 'landing.html')




def registro(request):
	if request.method == 'POST':
		info = informacion()
		info.nombre = request.POST['nombre']
		info.correo = request.POST['correo']
		info.telefono = request.POST['telefono']
		info.pais = request.POST['pais']
		
		info.save()
		return redirect('index:landing')
		
			




@login_required
def logout_view(request):
	#vistadel log out 
	logout(request)
	return redirect('index:landing')
		


class IndexView(TemplateView):
    template_name = "index.html"

