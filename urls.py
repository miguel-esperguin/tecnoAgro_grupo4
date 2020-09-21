from django.urls import path
from . import views

urlpatterns= [
	path('', views.home, name='home'),
	path('contacto/', views.consultar, name='consultar'),
	path('somos/', views.somos, name='somos'),
	path('aplicaciones/', views.aplicaciones, name='aplicaciones'),
	path('registro/', views.registro, name='registro'),
	path('descargas/', views.descargas, name='descargas'),
]