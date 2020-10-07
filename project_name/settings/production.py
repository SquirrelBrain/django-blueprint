"""
Production Settings & Configuration

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
    'www.example.com',
    'subdomain.example.com',
]

CSRF_COOKIE_AGE = 31449600

CSRF_COOKIE_DOMAIN = '.example.com'

CSRF_COOKIE_NAME = 'X_CSRF_Token'

CSRF_COOKIE_SECURE = True

CSRF_USE_SESSIONS = True

CSRF_HEADER_NAME = 'HTTP_X_XSRF_TOKEN'

CSRF_TRUSTED_ORIGINS = [
    '.example.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database_name',
        'USER': 'my_database_user',
        'PASSWORD': 'my_database_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

DEBUG = False

DEFAULT_FROM_EMAIL = 'DoNotReply@example.com'

DISALLOWED_USER_AGENTS = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'my_email_host@_provider.com'

EMAIL_HOST_PASSWORD = 'email_host_user_password'

EMAIL_HOST_USER = 'email_host_user'

EMAIL_PORT = 587

EMAIL_SUBJECT_PREFIX = '[MY_APP_NAME] '

EMAIL_USE_SSL = False

EMAIL_USE_TLS = True

EMAIL_SSL_CERTFILE = '/path/to/ssl_certfile.cer'

EMAIL_SSL_KEYFILE = '/path/to/ssl_certfile.cer'

INTERNAL_IPS = [
    '10.10.10.1'
]

OGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
            '%(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {'level': 'INFO', 'handlers': ['console']},
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins'],
            'propagate': True,
        },
    },
}

MANAGERS = [
    ('John Doe', 'john.doe@example.com'),
    ('Jane Doe', 'jane.doe@example.com'),
]

try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError as exc:
    raise KeyError(
        'Failed to load Django Secret Key!'
    ) as exc

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

# ============================== #
#            Sessions            #
# ============================== #
SESSION_COOKIE_AGE = 1209600

SESSION_COOKIE_DOMAIN = CSRF_COOKIE_DOMAIN

SESSION_COOKIE_HTTPONLY = True

SESSION_COOKIE_SECURE = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
