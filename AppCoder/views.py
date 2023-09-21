from django.shortcuts import render
from django.http import HttpResponse
from .models import Profesor


# Create your views here.
def profe_nuevo(request):
    profeN = Profesor (nombre= "Pepe", apellido = "Python", email = "pepe@python.com", profesion = "Biofisico")
    profeN.save
    
    return HttpResponse (f"Hemos guardado al profesor {profeN.nombre}")