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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Import variables for our application. Basically all imported variables
# have a SECRET_* prefix.
try:
    from ecantina_project.secret_settings import *
except ImportError:
    pass

# Import all constants to use throughout our application
try:
    from ecantina_project.constants import *
except ImportError:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = SECRET_DEBUG

ALLOWED_HOSTS = SECRET_ALLOWED_HOSTS

# 'Sites Framework' requires this line.
SITE_ID = 1

# The address domain URL.
SITE_DOMAIN_URL = "http://www.comicscantina.com"

# The Google Analytics Key
GOOGLE_ANALYTICS_KEY = SECRET_GOOGLE_ANALYTICS_KEY

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'rest_framework',
    'rest_framework.authtoken',
    'captcha',
    'paypal.standard.ipn',
    'inventory_base',
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
    'api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'ecantina_project.middleware.ECantinaSubDomainMiddleware',
#    'django.middleware.cache.UpdateCacheMiddleware',    # per-site cache
#    'django.middleware.common.CommonMiddleware',        # per-site cache
#    'django.middleware.cache.FetchFromCacheMiddleware', # per-site cache
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
# https://docs.djangoproject.com/en/1.8/topics/cache/
#
CACHES = {
    'default': { # (PROD/QA)
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
#    'default': { # (DEV)
#        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#    }
}



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ecantina_db",
        "USER": SECRET_DB_USER,
        "PASSWORD": SECRET_DB_PASSWORD,
        "HOST": SECRET_DB_HOST,
        "PORT": SECRET_DB_PORT,
    }
}



# Email
# http://stackoverflow.com/questions/19264907/python-django-gmail-smtp-setup

EMAIL_USE_TLS = True
EMAIL_HOST = SECRET_EMAIL_HOST
EMAIL_PORT = SECRET_EMAIL_PORT
EMAIL_HOST_USER = SECRET_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = EMAIL_HOST_USER



# Captcha App (Third Party)
# http://django-simple-captcha.readthedocs.org/en/latest/advanced.html

if 'test' in sys.argv:
    CAPTCHA_TEST_MODE = True
CAPTCHA_FONT_SIZE = 52



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
)


# User uploaded content.
#

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


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
PAYPAL_RECEIVER_EMAIL = SECRET_PAYPAL_RECEIVER_EMAIL
PAYPAL_TEST = SECRET_PAYPAL_TEST


# External Servers
#
COMICS_CANTINA_IMAGE_SERVER_ADDRESS = "https://www.comicscantina.com/img/"