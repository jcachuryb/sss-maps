"""Django settings for the Kaartdijin Boodja project.

Generated by `django-admin startproject` using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


# Standard
import os
import pathlib
import platform
import json 
import sys

# Third-Party
import decouple
import dj_database_url


# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / "staticfiles"

PRIVATE_MEDIA_URL = '/'
PRIVATE_MEDIA_ROOT = os.path.join(BASE_DIR, 'private-media')

# Project specific settings
PROJECT_TITLE = "SSS Maps"
PROJECT_DESCRIPTION = "DBCA System to store and serve files"
PROJECT_VERSION = "v1"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't allow all hosts in production!
SECRET_KEY = decouple.config("SECRET_KEY")
DEBUG = decouple.config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS=[""]
if DEBUG is True:
    ALLOWED_HOSTS=["*"]
else: 
    ALLOWED_HOSTS_STRING = decouple.config("ALLOWED_HOSTS", default='[""]')
    ALLOWED_HOSTS = json.loads(ALLOWED_HOSTS_STRING)

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "webtemplate_dbca",
    "sss_maps",
    "rest_framework",
    "rest_framework_datatables",
    "drf_spectacular",
    "django_filters",
    "django_cron",
    "appmonitor_client",
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "dbca_utils.middleware.SSOLoginMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "sss_maps.middleware.CacheControl",
    'django.middleware.locale.LocaleMiddleware',
]
ROOT_URLCONF = "sss_maps.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "sss_maps/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sss_maps.context_processors.variables",
            ],
        },
    },
]
WSGI_APPLICATION = "sss_maps.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": decouple.config("DATABASE_URL", cast=dj_database_url.parse, default="sqlite://memory"),
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db/db.sqlite3',
#     }
# }  
# print (DATABASES)
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = "en-au"
#TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "sss_maps/static",  # Look for static files in the frontend
    # BASE_DIR / "govapp/frontend/node_modules"  # node modules that are collected and used in the frontend
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Caching settings
# https://docs.djangoproject.com/en/3.2/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "cache",
        "OPTIONS": {"MAX_ENTRIES": 10000},
    }
}

# DBCA Template Settings
# https://github.com/dbca-wa/django-base-template/blob/main/govapp/settings.py
DEV_APP_BUILD_URL = decouple.config("DEV_APP_BUILD_URL", default=None)
ENABLE_DJANGO_LOGIN = decouple.config("ENABLE_DJANGO_LOGIN", default=False, cast=bool)
LEDGER_TEMPLATE = "bootstrap5"
GIT_COMMIT_HASH = os.popen(f"cd {BASE_DIR}; git log -1 --format=%H").read()  # noqa: S605
GIT_COMMIT_DATE = os.popen(f"cd {BASE_DIR}; git log -1 --format=%cd").read()  # noqa: S605
VERSION_NO = "2.00"

# Django REST Framework Settings
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}

# DRF Spectacular Settings
# https://drf-spectacular.readthedocs.io/en/latest/settings.html
SPECTACULAR_SETTINGS = {
    "TITLE": PROJECT_TITLE,
    "DESCRIPTION": PROJECT_DESCRIPTION,
    "VERSION": PROJECT_VERSION,
    "SERVE_INCLUDE_SCHEMA": True,
    "POSTPROCESSING_HOOKS": [],
    "COMPONENT_SPLIT_REQUEST": True,
}

path_to_logs = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(path_to_logs):
    os.mkdir(path_to_logs)

# Logging
# https://docs.djangoproject.com/en/3.2/topics/logging/
LOGGING = {
    "version": 1,
    'formatters': {
        'verbose2': {
            "format": "%(levelname)s %(asctime)s %(name)s [Line:%(lineno)s][%(funcName)s] %(message)s"
        }
    },
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose2',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'sss_maps.log'),
            'formatter': 'verbose2',
            'maxBytes': 5242880
        },
        'file_for_sql': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'sss_maps_sql.log'),
            'formatter': 'verbose2',
            'maxBytes': 5242880
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        # Log SQL
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['file_for_sql'],
        #     'propagate': False,
        # },
    }
}
ENABLE_SQL_LOGGING = decouple.config("ENABLE_SQL_LOGGING", default=False, cast=bool)
if ENABLE_SQL_LOGGING:
    LOGGING['loggers']['django.db.backends'] = {
        'level': 'DEBUG',
        'handlers': ['file_for_sql'],
        'propagate': False,
    }


# Email
#DISABLE_EMAIL = decouple.config("DISABLE_EMAIL", default=False, cast=bool)
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = "wagov_utils.components.utils.email_backend.EmailBackend"
EMAIL_HOST = decouple.config("EMAIL_HOST", default="smtp.lan.fyi")
EMAIL_PORT = decouple.config("EMAIL_PORT", default=25, cast=int)
DEFAULT_FROM_EMAIL = "no-reply@dbca.wa.gov.au"
EMAIL_INSTANCE = decouple.config("EMAIL_INSTANCE", default="PROD")
NON_PROD_EMAIL = decouple.config("NON_PROD_EMAIL", default="")
PRODUCTION_EMAIL= decouple.config("PRODUCTION_EMAIL", default=False, cast=bool)
EMAIL_DELIVERY = decouple.config("EMAIL_DELIVERY", default="off")

# Group Settings
GROUP_API_USERS = decouple.config("GROUP_API_USERS", default='SSSApiUsers')

# Cron Jobs
# https://django-cron.readthedocs.io/en/latest/installation.html
# https://django-cron.readthedocs.io/en/latest/configuration.html
#CRON_SCANNER_CLASS = "govapp.apps.catalogue.cron.ScannerCronJob"

CRON_CLASSES = [
    'appmonitor_client.cron.CronJobAppMonitorClient'
]
MANAGEMENT_COMMANDS_PAGE_ENABLED = decouple.config('MANAGEMENT_COMMANDS_PAGE_ENABLED', default=False)

# Temporary Fix for ARM Architecture
if platform.machine() == "arm64":
    GDAL_LIBRARY_PATH = "/opt/homebrew/opt/gdal/lib/libgdal.dylib"
    GEOS_LIBRARY_PATH = "/opt/homebrew/opt/geos/lib/libgeos_c.dylib"

# Django Timezone
TIME_ZONE = 'Australia/Perth'
# DATE_FORMAT = 'dd/mm/YYYY'
# DATETIME_FORMAT = 'dd/mm/YYYY HH:ii:ss'
# SHORT_DATE_FORMAT = 'dd/mm/YY'
# SHORT_DATETIME_FORMAT = 'dd/mm/YY HH:ii'

APPLICATION_VERSION = decouple.config("APPLICATION_VERSION", default="1.0.0" + "-" + GIT_COMMIT_HASH[:7])
RUNNING_DEVSERVER = len(sys.argv) > 1 and sys.argv[1] == "runserver"

CSRF_TRUSTED_ORIGINS_STRING = decouple.config("CSRF_TRUSTED_ORIGINS", default='[]')
CSRF_TRUSTED_ORIGINS = json.loads(str(CSRF_TRUSTED_ORIGINS_STRING))

BYPASS_AUTHENTICATION = decouple.config("BYPASS_AUTHENTICATION", default=False)
