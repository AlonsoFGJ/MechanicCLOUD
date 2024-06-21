"""
WSGI config for Pagina project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Añadir el directorio actual al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ajustar el nombre del módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pagina.settings")

# Configuración de Django
application = get_wsgi_application()
