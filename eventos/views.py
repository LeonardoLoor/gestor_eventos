from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Importar messages
from django.db.models import Q

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
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento})

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
    return render(request, 'eventos/editar_evento.html', {'form': form})

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, creador=request.user)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento eliminado correctamente.')
        return redirect('lista_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

