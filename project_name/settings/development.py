"""
Development Settings & Configuration

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# flake8: noqa
from .base import *


# ============================== #
#          Core Settings         #
# ============================== #
ALLOWED_HOSTS = [
    'locahost',
    '0.0.0.0',
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(PROJECT_ROOT / 'db.sqlite3'),
        'TEST': {
            'NAME': str(PROJECT_ROOT / 'test.sqlite3'),
        },
    }
}

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_TIMEOUT = 60

INSTALLED_APPS += [

    # Django Admin Documentation
    'django.contrib.admindocs',

    # Django Debug Toolbar
    'debug_toolbar',

]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
            '%(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']},
}

MANAGERS = ADMINS

MIDDLEWARE += [

    # Django Debug Toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

SECRET_KEY = '{{ secret_key }}'

# ============================== #
#            Sessions            #
# ============================== #
SESSION_COOKIE_AGE = 2629746

SESSION_COOKIE_HTTPONLY = False

SESSION_COOKIE_SECURE = False

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
