"""
Django settings for project.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import logging.config  # noqa: E402
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = 'blog.User'

IS_DOCKER = os.environ.get('IS_DOCKER', False)

### Print variables ###
print(f'=== {BASE_DIR=}')  # noqa: T201
print(f"=== {os.environ['DJANGO_SETTINGS_MODULE']=}")  # noqa: T201
### End: Print variables ###

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS: list[str] = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsecure')

# Static
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'

# Media
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Imported apps.
    'blog',
]

# Ordering is important.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS':
            {
                'context_processors':
                    [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
            },
    },
]

WSGI_APPLICATION = 'root.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # default
]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Oslo'
USE_I18N = False
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

### DRF ###
INSTALLED_APPS += [
    'rest_framework',
]
# https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication'],
    'DEFAULT_PERMISSION_CLASSES':
        [
            # 'rest_framework.permissions.IsAuthenticated',
            # 'rest_framework.permissions.DjangoObjectPermissions',
            'blog.custom_classes.permission_classes.CustomDjangoObjectPermissions',
        ]
}

BYPASS_AUTHENTICATION = os.environ.get('BYPASS_AUTHENTICATION') == 'yes'
if BYPASS_AUTHENTICATION:
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ['rest_framework.permissions.AllowAny']

### End: DRF ###

### django-extensions ###
INSTALLED_APPS += [
    'django_extensions',
]
### End: django-extensions ###

### django-guardian ###
INSTALLED_APPS += [
    'guardian',
]
AUTHENTICATION_BACKENDS += [
    'guardian.backends.ObjectPermissionBackend',
]
### End: django-guardian ###

### admin_auto_filters ###
INSTALLED_APPS += [
    'admin_auto_filters',
]
### End: admin_auto_filters ###

################## LOGGING ##################

LOGFILENAME = BASE_DIR / 'logs' / 'server.log'
SQL_LOG_FILE = BASE_DIR / 'logs' / 'sql.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':
        {
            'file': {
                'format': '%(asctime)s  %(name)s  %(levelname)s  %(message)s',
            },
            'pretty': {
                'format': '\n[%(levelname)s]  %(asctime)s  (%(name)s):\n- %(message)s\n',
            },
        },
    'filters':
        {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
    'handlers':
        {
            'null': {
                'class': 'logging.NullHandler',
            },
            'console':
                {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'pretty',
                    'filters': ['require_debug_true'],
                },
            'file':
                {
                    'level': 'INFO',
                    'class': 'logging.FileHandler',
                    'formatter': 'file',
                    'mode': 'w',  # Reset file each time server reloads.
                    'filename': LOGFILENAME,
                    'filters': ['require_debug_true'],
                },
            'sql_file':
                {
                    'level': 'DEBUG',
                    'class': 'logging.FileHandler',
                    'filename': SQL_LOG_FILE,  # Added to '.gitignore'.
                    'mode': 'w',  # Reset file each time server reloads.
                    'filters': ['require_debug_true'],
                },
        },
    'loggers':
        {
            # Default logger.
            '': {
                'handlers': ['console', 'file'],
                'propagate': True,
                'level': 'INFO',
            },
            # Catch all from django unless explicitly prevented propagation.
            'django': {
                'handlers': ['console', 'file'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'django.db.backends':
                {
                    'handlers': ['sql_file'],
                    'propagate': False,  # Don't pass up to 'django'.
                    'level': 'DEBUG',
                },
            'django.server':
                {
                    'handlers': ['console', 'file'],
                    'propagate': False,  # Don't pass up to 'django'.
                    'level': 'INFO',
                },
            'django.utils.autoreload':
                {
                    'handlers': ['console', 'file'],
                    'propagate': False,  # Don't pass up to 'django'.
                    'level': 'INFO',
                },
        },
}

logging.config.dictConfig(LOGGING)

# Quick fix for avoiding concurrency issues related to db access
# Note: this might not be an ideal solution. See these links for information
# https://docs.djangoproject.com/en/1.10/topics/db/transactions/#django.db.transaction.on_commit
# https://medium.com/@hakibenita/how-to-manage-concurrency-in-django-models-b240fed4ee2
ATOMIC_REQUESTS = True
APPEND_SLASH = True

### Database ###
DOCKER_DB_NAME = 'docker.db.sqlite3'
LOCAL_DB_NAME = 'db.sqlite3'
DB_NAME = DOCKER_DB_NAME if IS_DOCKER else LOCAL_DB_NAME

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database' / DB_NAME,
    }
}
### End: Database ###