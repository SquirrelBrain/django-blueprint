# Django's Command-Line Utility for executing Administrative Tasks
# Docs: https://docs.djangoproject.com/en/{{ docs_version }}/ref/django-admin/

import os
import sys


if __name__ == '__main__':

    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        '{{ project_name }}.settings.development'
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as Exc:
        raise ImportError(
            'Failed to import Django Web Framework. Did you activate '
            'your Virtual Environment? Is Django installed and available '
            'on your PYTHONPATH?'
        ) from Exc
    execute_from_command_line(sys.argv)
