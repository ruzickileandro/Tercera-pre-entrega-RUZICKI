from unidecode import unidecode
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Evento
from .forms import EventoForm

def lista_eventos(request):
    eventos = Evento.objects.all()
    context = {
        'eventos': eventos
    }
    return render(request, 'Home/base.html', context)


def crear_evento(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/")
    else: 
        form = EventoForm()
    return render(request, "evento/crear_evento.html", {"form": form})



def buscar_eventos(request):
    query = request.GET.get('q', '')
    eventos = None

    if query:
        query_normalized = unidecode(query.lower())  # Convertir a minúsculas y luego aplicar unidecode

        eventos = Evento.objects.filter(titulo__icontains=query_normalized) | Evento.objects.filter(descripcion__icontains=query_normalized)

    return render(request, 'evento/buscar_eventos.html', {'eventos': eventos, 'query': query})

