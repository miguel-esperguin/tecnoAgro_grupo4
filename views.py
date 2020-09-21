from django.shortcuts import render
from django.utils import timezone
from .models import Consulta
 


# Create your views here.
def consultar(request):
   return render(request, 'consultar.html', {})

def home(request):
	return render(request, 'home_tecnoagro.html', {})

def somos(request):
	return render(request, 'quienessomos.html', {})

def aplicaciones(request):
	return render(request, 'aplicaciones.html', {})

def registro(request):
	return render(request, 'registro.html', {})

def descargas(request):
	return render(request, 'descargas.html', {})