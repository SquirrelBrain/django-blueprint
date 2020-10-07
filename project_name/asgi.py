"""
Asynchronous Server Gateway Interface (ASGI)
Docs: https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      '{{ project_name }}.settings.production')

application = get_asgi_application()
