from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login

#revisar vistas basadas en clases



def landingPage(request):
	
	return render(request, 'landing.html')


class IndexView(TemplateView):
    template_name = "index.html"

