"""
WSGI config for acme_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

Para obtener más información acerca de este archivo, consulta
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acme_project.settings')

application = get_wsgi_application()
