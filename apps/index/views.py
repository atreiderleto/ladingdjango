from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
#modelo usuario
from django.contrib.auth.models import User
from apps.index.models import usuario



def landingPage(request):
	return render(request, 'landing.html')




def registro(request):
	#vista del registro
	if request.method == 'POST':
		nombre = request.POST['nombre']
		correo = request.POST['correo']
		telefono = request.POST['telefono']
		pais = request.POST['pais']
	



@login_required
def logout_view(request):
	#vistadel log out 
	logout(request)
	return redirect('index:landing')
		


class IndexView(TemplateView):
    template_name = "index.html"

