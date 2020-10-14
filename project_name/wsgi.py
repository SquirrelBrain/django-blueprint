"""
Web Server Gateway Interface (WSGI)
Docs: https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      '{{ project_name }}.settings.production')

application = get_wsgi_application()
