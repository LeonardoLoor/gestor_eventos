"""
ASGI config for gestor_eventos project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Establezco la configuración predeterminada para el entorno ASGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor_eventos.settings')

# Obtengo la aplicación ASGI para el proyecto
application = get_asgi_application()

