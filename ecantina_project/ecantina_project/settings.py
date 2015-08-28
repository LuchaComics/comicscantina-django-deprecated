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
    'inventory', # Deprecated
    'inventory_base',
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
    'etl',
    'store_base',
    'store_landpage',
    'store_about',
    'store_products',
    'store_blog',
    'store_checkout',
    'store_customer',
    'register',
    'login',
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



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ecantina_db",
        "USER": "django",
        "PASSWORD": "123password",
        "HOST": "localhost",
        "PORT": "5432",
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



# Captcha App
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


# JavaScript Libraries
#
INVENTORY_CSS_LIBRARY= [
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/fontawesome/css/font-awesome.min.css", "id":"",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/simple-line-icons/css/simple-line-icons.css", "id":"",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/animate.css/animate.min.css", "id":"",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/bootstrap.css", "id":"bscss",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/js/jquery/jquery-ui/jquery-ui.css", "id":"",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/js/jquery/jquery-ui/jquery-ui.structure.css", "id":"",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/js/jquery/jquery-ui/jquery-ui.theme.css", "id":"",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/app.css", "id":"maincss",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/theme-e.css", "id":"themecss",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/comicscantina.css", "id":"comicscantinacss",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/jquery.filer.css", "id":"jqfiler",},
    {"type":"text/css", "rel":"stylesheet", "href":"inventory/css/themes/jquery.filer-dragdropbox-theme.css", "id":"jqfilertheme",},
                        ]

INVENTORY_JS_LIBRARY_HEADER = [
    {"type":"text/javascript", "src":"inventory/js/jquery/dist/jquery.js",},
    {"type":"text/javascript", "src":"inventory/js/bootstrap/dist/js/bootstrap.js",},
]

INVENTORY_JS_LIBRARY_BODY = [
    {"type":"text/javascript", "src":"inventory/js/modernizr/modernizr.js",},
    {"type":"text/javascript", "src":"inventory/js/jquery/dist/jquery.js",},
    {"type":"text/javascript", "src":"inventory/js/jquery/jquery-ui/jquery-ui.js",},
    {"type":"text/javascript", "src":"inventory/js/bootstrap/dist/js/bootstrap.js",},
    {"type":"text/javascript", "src":"inventory/js/jquery/jquery.easing/js/jquery.easing.js",},
    {"type":"text/javascript", "src":"inventory/js/animo.js/animo.js",},
    #{"type":"text/javascript", "src":"inventory/vendor/jquery-localize-i18n/dist/jquery.localize.js",},
    {"type":"text/javascript", "src":"inventory/js/jQuery-Storage-API/jquery.storageapi.js",},
    {"type":"text/javascript", "src":"inventory/js/slimScroll/jquery.slimscroll.min.js",},
    {"type":"text/javascript", "src":"inventory/js/sparklines/jquery.sparkline.min.js",},
    {"type":"text/javascript", "src":"inventory/js/Flot/jquery.flot.js",},
    {"type":"text/javascript", "src":"inventory/js/flot.tooltip/js/jquery.flot.tooltip.min.js",},
    {"type":"text/javascript", "src":"inventory/js/Flot/jquery.flot.resize.js",},
    {"type":"text/javascript", "src":"inventory/js/Flot/jquery.flot.categories.js",},
    {"type":"text/javascript", "src":"inventory/js/flot-spline/js/jquery.flot.spline.min.js",},
    {"type":"text/javascript", "src":"inventory/js/ika.jvectormap/jquery-jvectormap-1.2.2.min.js",},
    {"type":"text/javascript", "src":"inventory/js/ika.jvectormap/jquery-jvectormap-world-mill-en.js",},
    {"type":"text/javascript", "src":"inventory/js/ika.jvectormap/jquery-jvectormap-us-mill-en.js",},
    {"type":"text/javascript", "src":"inventory/js/flot-annual_sales_chart.js",},
    {"type":"text/javascript", "src":"inventory/js/dropzone/dropzone.js",},
    {"type":"text/javascript", "src":"inventory/js/app.js",},
    {"type":"text/javascript", "src":"inventory/js/jquery.filer.min.js",},
]

STORE_CSS_LIBRARY= [
    {"type":"text/css", "rel":"stylesheet", "href":"store/bootstrap/css/bootstrap.css", "id":"",},
    {"type":"text/css", "rel":"stylesheet", "href":"store/css/style.css", "id":"",},
    {"type":"text/css", "rel":"stylesheet", "href":"store/css/story.css", "id":"",},
]

STORE_JS_LIBRARY_HEADER = [
    {"type":"text/javascript", "src":"store/inventory/jquery/dist/jquery.js",},
    {"type":"text/javascript", "src":"store/inventory/bootstrap/dist/js/bootstrap.js",},
    {"type":"text/javascript", "src":"store/js/pace.min.js",},
]

STORE_JS_LIBRARY_BODY = [
    {"type":"text/javascript", "src":"store/js/jquery/jquery-1.10.1.min.js",},
    {"type":"text/javascript", "src":"store/bootstrap/js/bootstrap.min.js",},
    {"type":"text/javascript", "src":"store/js/jquery.parallax-1.1.js",},
    {"type":"text/javascript", "src":"store/js/helper-plugins/jquery.mousewheel.min.js",},
    {"type":"text/javascript", "src":"store/js/jquery.mCustomScrollbar.js",},
    {"type":"text/javascript", "src":"store/js/ion-checkRadio/ion.checkRadio.min.js",},
    {"type":"text/javascript", "src":"store/js/grids.js",},
    {"type":"text/javascript", "src":"store/js/owl.carousel.min.js",},
    {"type":"text/javascript", "src":"store/js/jquery.minimalect.min.js",},
    {"type":"text/javascript", "src":"store/js/bootstrap.touchspin.js",},
    {"type":"text/javascript", "src":"store/js/script.js",},
    {"type":"text/javascript", "src":"store/js/skrollr.min.js",},
]


# Custom Constants
#
EMPLOYEE_OWNER_ROLE = 0
EMPLOYEE_MANAGER_ROLE = 1
EMPLOYEE_WORKER_ROLE = 2

# Product Types
COMIC_PRODUCT_TYPE = 1
FURNITURE_PRODUCT_TYPE = 2
COIN_PRODUCT_TYPE = 3
GENERAL_PRODUCT_TYPE = 4

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    )
}