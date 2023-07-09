from django.shortcuts import render
from .models import Evento

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'evento/index.html', {'eventos': eventos})