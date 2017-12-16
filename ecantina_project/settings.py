"""
    Django settings for ecantina_project project.

    Generated by 'django-admin startproject' using Django 1.8.

    For more information on this file, see
    https://docs.djangoproject.com/en/1.8/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/1.8/ref/settings/
    """

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

"""
Add support for .env files.
"""
import dj_database_url
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def env_var(key, default=None):
    """Retrieves env vars and makes Python boolean replacements"""
    val = os.environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))


# Import all constants to use throughout our application
try:
    from ecantina_project.constants import *
except ImportError:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_var("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_var("IS_DEBUG")

ALLOWED_HOSTS = [env_var("ALLOWED_HOSTS")]

# The person to contact on error when DEBUG=False
ADMINS = [(env_var("ADMIN_NAME"), env_var("ADMIN_EMAIL")),]

# 'Sites Framework' requires this line.
SITE_ID = 1

# The Google Analytics Key
GOOGLE_ANALYTICS_KEY = env_var("GOOGLE_ANALYTICS_KEY")

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition




# Application definition
#
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'storages',
    'compressor',
    'sorl.thumbnail',
    'rest_framework',
    'rest_framework.authtoken',
    'paypal.standard.ipn',
    'inventory_base',
    'inventory_catalog',
    'inventory_login',
    'inventory_products',
    'inventory_checkout',
    'inventory_order',
    'inventory_help',
    'inventory_customer',
    'inventory_print_label',
    'inventory_dashboard',
    'inventory_setting',
    'inventory_email',
    'inventory_pulllist',
    'inventory_register',
    'inventory_wishlist',
    'mobile_pos',
    'etl',
    'store_base',
    'store_landpage',
    'store_about',
    'store_products',
    'store_blog',
    'store_checkout',
    'store_customer',
    'store_register',
    'store_help',
    'store_search',
    'api',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',        # per-site cache
    'htmlmin.middleware.HtmlMinifyMiddleware',               # HTML Minify
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'ecantina_project.custom_middleware.ECantinaSubDomainMiddleware',
    'ecantina_project.mobile_middleware.MobileDeviceDetectorMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',     # per-site cache
    'htmlmin.middleware.MarkRequestMiddleware',              # HTML Minify
)

ROOT_URLCONF = 'ecantina_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
},
]

WSGI_APPLICATION = 'ecantina_project.wsgi.application'



# Django Caching
# https://docs.djangoproject.com/en/dev/topics/cache/

CACHES = {
    'default': { # (PROD/QA)
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': '300',
    }
    # 'default': { # (DEV)
    #    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    # }
}



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        "ENGINE": "django.db.backends.postgresql_psycopg2"
    }
}
DATABASES['default'] = dj_database_url.config(default=env_var("DATABASE_URL"))



# Email
#

EMAIL_BACKEND = env_var("EMAIL_BACKEND")
MAILGUN_ACCESS_KEY = env_var("MAILGUN_ACCESS_KEY")
MAILGUN_SERVER_NAME = env_var("MAILGUN_SERVER_NAME")
DEFAULT_FROM_EMAIL = env_var("DEFAULT_FROM_EMAIL")
DEFAULT_TO_EMAIL = env_var("DEFAULT_TO_EMAIL")
APPEND_SLASH=False



# Error Emailing
# https://docs.djangoproject.com/en/dev/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False, # Set to this value to prevent spam
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Django-Storages
#
AWS_STORAGE_BUCKET_NAME = env_var("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = env_var("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env_var("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_USE_SSL = False


# Static files (CSS, JavaScript, Images) + Django-Storages
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'ecantina_project.custom_storage.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'ecantina_project.custom_storage.MediaStorage'

MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ecantina_project', 'static'),
)



# Django REST Framework Configuration (Third Party)
#
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    )
}



# PayPal
#

PAYPAL_RECEIVER_EMAIL = env_var("PAYPAL_RECEIVER_EMAIL")
PAYPAL_TEST = env_var("PAYPAL_TEST")



# External Servers
#

COMICS_CANTINA_IMAGE_SERVER_BASE_URL = env_var("COMICS_CANTINA_IMAGE_SERVER_BASE_URL")



# django-htmlmin
# https://github.com/cobrateam/django-htmlmin

HTML_MINIFY = env_var("HTML_MINIFY")
KEEP_COMMENTS_ON_MINIFYING = env_var("KEEP_COMMENTS_ON_MINIFYING")



# Django-Compressor
# http://django-compressor.readthedocs.org/en/latest/settings/

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.rCSSMinFilter',]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_ENABLED = env_var("COMPRESS_ENABLED")



# Django-Compressor + Django-Storages
#

COMPRESS_STORAGE = 'ecantina_project.custom_storage.CachedS3BotoStorage'


# sorl-thumbnail
# https://github.com/mariocesar/sorl-thumbnail

THUMBNAIL_ENGINE = 'ecantina_project.snorlthumbnailutils.Engine'
THUMBNAIL_DEBUG=True
THUMBNAIL_FORCE_OVERWRITE = True
