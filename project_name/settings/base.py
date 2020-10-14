"""
Core Settings & Configuration for Django

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

from pathlib import Path
from sys import path


# ============================== #
#           Filesystem           #
# ============================== #
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

APPS_DIR = Path(PROJECT_ROOT).joinpath('apps')

LOG_DIR = Path(PROJECT_ROOT).joinpath('logs')

MEDIA_ROOT = Path(PROJECT_ROOT).joinpath('media')

SCRIPTS_DIR = Path(PROJECT_ROOT).joinpath('scripts')

STATIC_ROOT = Path(PROJECT_ROOT).joinpath('assets')

for directory in [APPS_DIR, LOG_DIR, MEDIA_ROOT, SCRIPTS_DIR]:
    if not Path(directory).exists():
        Path(directory).mkdir()
    path.append(directory)

# ============================== #
#          Core Settings         #
# ============================== #
ADMINS = [
    ('John Doe', 'john.doe@example.com'),
    ('Jane Doe', 'jane.doe@example.com'),
]

FIXTURE_DIRS = [
    Path(PROJECT_ROOT).joinpath('fixtures'),
]

INSTALLED_APPS = [

    # Django Core Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party Apps

    # Custom Apps

]

MEDIA_URL = '/site-media/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'

SERVER_EMAIL = 'DoNotReply@server_fqdn.com'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            Path(PROJECT_ROOT).joinpath('templates'),
        ],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
# ============================== #
#              Auth              #
# ============================== #
AUTH_USER_MODEL = 'auth.User'

LOGIN_URL = '/accounts/login/'

LOGOUT_REDIRECT_URL = LOGIN_URL

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # noqa: E501
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},            # noqa: E501
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},           # noqa: E501
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},          # noqa: E501
]

# ============================== #
#            Sessions            #
# ============================== #
SESSION_COOKIE_NAME = 'X_Session_ID'

# ============================== #
#              Sites             #
# ============================== #
SITE_ID = 100

# ============================== #
#           Static Files         #
# ============================== #
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    Path(PROJECT_ROOT).joinpath('static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
