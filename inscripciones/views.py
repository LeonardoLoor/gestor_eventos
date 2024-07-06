from django.shortcuts import render, redirect, get_object_or_404
from .models import Inscripcion
from eventos.models import Evento
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Función para enviar un correo de confirmación de inscripción
def enviar_correo_confirmacion_inscripcion(usuario, evento):
    subject = 'Confirmación de Inscripción'
    message = f'Hola {usuario.nombre},\n\nTe has inscrito correctamente al evento: {evento.nombre}.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [usuario.email]
    send_mail(subject, message, email_from, recipient_list)

# Vista protegida que permite a un usuario inscribirse a un evento
@login_required
def inscribir(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)  # Obtener el evento por ID o devolver un error 404 si no existe
    Inscripcion.objects.create(evento=evento, usuario=request.user)  # Crear una nueva inscripción para el usuario autenticado
    return redirect('mis_eventos')  # Redirigir a la página de mis eventos

# Vista protegida que muestra los eventos en los que el usuario está inscrito
@login_required
def mis_eventos(request):
    inscripciones = Inscripcion.objects.filter(usuario=request.user)  # Obtener todas las inscripciones del usuario autenticado
    return render(request, 'inscripciones/mis_eventos.html', {'inscripciones': inscripciones})  # Renderizar la plantilla 'mis_eventos.html' con las inscripciones
