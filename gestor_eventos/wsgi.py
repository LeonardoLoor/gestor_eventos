"""
WSGI config for gestor_eventos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Establezco la configuración predeterminada para el entorno WSGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor_eventos.settings')

# Obtengo la aplicación WSGI para el proyecto
application = get_wsgi_application()

