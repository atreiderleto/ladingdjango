from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

#modelo usuario
from django.contrib.auth.models import User





def landingPage(request):
	return render(request, 'landing.html')


def registro(request):
	#registro de usuario
	return render(request, 'nav-bar.html')

	
		
# if request.method == 'POST':
# 		username = request.POST['usuario']
# 		correo = request.POST['correo']
# 		telefono = request.POST['telefono']
# 		pais = request.POST['pais']

# 		if user == '' or correo =='' or telefono == '' or pais == '':
# 			return render(request, 'form-modal.html', {'error': 'Todos los campos son obligatorios'})
		

class IndexView(TemplateView):
    template_name = "index.html"

