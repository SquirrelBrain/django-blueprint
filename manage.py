"""
Django's Command-Line Utility for executing Administrative Tasks
Docs: https://docs.djangoproject.com/en/dev/ref/django-admin/
"""

import os
import sys


def execute_subcommand():
    """
    Execute Administrative Subcommand
    Usage: python3 manage.py <sub_command> <options>
    """

    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          '{{ project_name }}.settings.development')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Failed to import Django Web Framework. Did you activate your '
            'Virtual Environment? Are you sure that Django is installed '
            'and available on your PYTHONPATH?'
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    execute_subcommand()
