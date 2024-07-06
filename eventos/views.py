# eventos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Vista para la página de inicio
def pagina_inicio(request):
    return render(request, 'eventos/pagina_inicio.html')

# Vista para listar los eventos
def lista_eventos(request):
    query = request.GET.get('q')  # Obtengo la consulta de búsqueda si existe
    if query:
        eventos_list = Evento.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    else:
        eventos_list = Evento.objects.all()  # Obtengo todos los eventos si no hay consulta de búsqueda

    paginator = Paginator(eventos_list, 10)  # Pagino los resultados, 10 eventos por página
    page_number = request.GET.get('page')  # Obtengo el número de página actual
    page_obj = paginator.get_page(page_number)  # Obtengo la página actual

    return render(request, 'eventos/lista_eventos.html', {'page_obj': page_obj, 'query': query})

# Vista para crear un evento
@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)  # Obtengo los datos del formulario
        if form.is_valid():
            evento = form.save(commit=False)  # Creo el evento sin guardarlo todavía
            evento.creador = request.user  # Asigno el creador del evento
            evento.save()  # Guardo el evento
            messages.success(request, 'El evento ha sido creado exitosamente.')
            return redirect('lista_eventos')
    else:
        form = EventoForm()  # Formulario vacío para GET
    return render(request, 'eventos/crear_evento.html', {'form': form})

# Vista para mostrar los detalles de un evento
def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)  # Obtengo el evento o muestro 404 si no existe
    inscrito = request.user in evento.inscritos.all()  # Verifico si el usuario está inscrito
    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'inscrito': inscrito})

# Vista para editar un evento
@login_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, creador=request.user)  # Obtengo el evento o muestro 404 si no existe
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)  # Formulario con datos existentes
        if form.is_valid():
            form.save()  # Guardo los cambios
            messages.success(request, 'Evento actualizado correctamente.')
            return redirect('detalle_evento', evento_id=evento.id)
    else:
        form = EventoForm(instance=evento)  # Formulario vacío para GET
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento_id': evento.id})

# Vista para eliminar un evento
@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, creador=request.user)  # Obtengo el evento o muestro 404 si no existe
    if request.method == 'POST':
        evento.delete()  # Elimino el evento
        messages.success(request, 'Evento eliminado correctamente.')
        return redirect('lista_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

# Vista para inscribirse o cancelar inscripción a un evento
@login_required
def inscribirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)  # Obtengo el evento o muestro 404 si no existe
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'inscribirse':
            evento.inscritos.add(request.user)  # Inscribo al usuario al evento
            messages.success(request, 'Te has inscrito exitosamente al evento.')
        elif action == 'cancelar':
            evento.inscritos.remove(request.user)  # Cancelo la inscripción del usuario al evento
            messages.success(request, 'Tu inscripción ha sido cancelada.')
        return redirect('detalle_evento', evento_id=evento.id)
    return render(request, 'eventos/inscribirse_evento.html', {'evento': evento})

# Vista para listar los eventos a los que el usuario está inscrito
@login_required
def eventos_inscritos(request):
    eventos = request.user.eventos_inscritos.all()  # Obtengo los eventos inscritos del usuario
    return render(request, 'eventos/eventos_inscritos.html', {'eventos': eventos})
