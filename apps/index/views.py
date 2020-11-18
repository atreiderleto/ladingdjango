from django.views.generic import TemplateView

#revisar vistas basadas en clases

class IndexView(TemplateView):
    template_name = "index.html"

