# eventos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from inscripciones.models import Inscripcion  # Importar el modelo de inscripción si aún no se ha hecho

def pagina_inicio(request):
    return render(request, 'eventos/pagina_inicio.html')

def lista_eventos(request):
    query = request.GET.get('q')
    if query:
        eventos_list = Evento.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    else:
        eventos_list = Evento.objects.all()

    paginator = Paginator(eventos_list, 10)  # Muestra 10 eventos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'eventos/lista_eventos.html', {'page_obj': page_obj, 'query': query})

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.creador = request.user
            evento.save()
            messages.success(request, 'El evento ha sido creado exitosamente.')
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    inscrito = request.user in evento.inscritos.all()
    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'inscrito': inscrito})

@login_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, creador=request.user)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento actualizado correctamente.')
            return redirect('detalle_evento', evento_id=evento.id)
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento_id': evento.id})

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, creador=request.user)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento eliminado correctamente.')
        return redirect('lista_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

@login_required
def inscribirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'inscribirse':
            evento.inscritos.add(request.user)
            messages.success(request, 'Te has inscrito exitosamente al evento.')
        elif action == 'cancelar':
            evento.inscritos.remove(request.user)
            messages.success(request, 'Tu inscripción ha sido cancelada.')
        return redirect('detalle_evento', evento_id=evento.id)
    return render(request, 'eventos/inscribirse_evento.html', {'evento': evento})

@login_required
def eventos_inscritos(request):
    eventos = request.user.eventos_inscritos.all()
    return render(request, 'eventos/eventos_inscritos.html', {'eventos': eventos})
