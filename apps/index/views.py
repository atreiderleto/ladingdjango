from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#modelo usuario
from django.contrib.auth.models import User





def landingPage(request):
	return render(request, 'landing.html')

	



def logout(request):
	if request.user.is_authenticated:
	#deslogear usuario
		logout(request)
		message.success(request, 'Tu seccion se Cerro con Exito')

	return redirect('index.views.logout')
	
		
	

class IndexView(TemplateView):
    template_name = "index.html"

