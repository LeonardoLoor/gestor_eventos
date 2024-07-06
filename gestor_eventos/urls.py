"""
URL configuration for gestor_eventos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from eventos import views as eventos_views

# Defino las URL del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el administrador de Django
    path('usuarios/', include('usuarios.urls')),  # Incluyo las URL del módulo de usuarios
    path('eventos/', include('eventos.urls')),  # Incluyo las URL del módulo de eventos
    path('inscripciones/', include('inscripciones.urls')),  # Incluyo las URL del módulo de inscripciones
    path('', eventos_views.pagina_inicio, name='pagina_inicio'),  # Ruta para la página de inicio
]

