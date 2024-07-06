from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.conf import settings
from .models import Usuario
from .forms import RegistroForm, LoginForm

# Vista para el registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Registro exitoso. ¡Bienvenido a Gestor de Eventos!')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Error en el registro: {e}')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f'Error en {field.label}: {error}')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista para el inicio de sesión de usuarios
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bienvenido, {username}')
                return redirect('pagina_inicio')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Error en el formulario. Por favor, intenta nuevamente.')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

# Vista para el cierre de sesión de usuarios
def logout(request):
    auth_logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')
