from django.urls import path
from . import views


app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
 	path('landing/', views.landingPage, name='landing'),
 	#path('registro/', views.registro, name='registro'),
 	path('logout/', views.logout, name='logout'),
]