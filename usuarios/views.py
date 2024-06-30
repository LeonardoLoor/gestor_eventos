from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Usuario
from .forms import RegistroForm

def enviar_correo_confirmacion(usuario):
    subject = 'Bienvenido a Gestor de Eventos'
    message = f'Hola {usuario.nombre},\n\nGracias por registrarte en Gestor de Eventos.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [usuario.email]
    send_mail(subject, message, email_from, recipient_list)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                enviar_correo_confirmacion(user)
                messages.success(request, 'Registro exitoso. Revisa tu correo electrónico para la confirmación.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Error en el registro: {e}')
        else:
            messages.error(request, 'Error en el registro. Por favor, intenta nuevamente.')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('lista_eventos')
        else:
            messages.error(request, 'Error en el inicio de sesión. Por favor, intenta nuevamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')
