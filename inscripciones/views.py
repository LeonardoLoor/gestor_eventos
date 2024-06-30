from django.shortcuts import render, redirect, get_object_or_404
from .models import Inscripcion
from eventos.models import Evento
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

def enviar_correo_confirmacion_inscripcion(usuario, evento):
    subject = 'Confirmación de Inscripción'
    message = f'Hola {usuario.nombre},\n\nTe has inscrito correctamente al evento: {evento.nombre}.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [usuario.email]
    send_mail(subject, message, email_from, recipient_list)

@login_required
def inscribir(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    Inscripcion.objects.create(evento=evento, usuario=request.user)
    return redirect('mis_eventos')

@login_required
def mis_eventos(request):
    inscripciones = Inscripcion.objects.filter(usuario=request.user)
    return render(request, 'inscripciones/mis_eventos.html', {'inscripciones': inscripciones})

