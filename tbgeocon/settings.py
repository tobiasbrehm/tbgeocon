"""
Django settings for tbgeocon project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import json

#
with open('/etc/config.json') as config_file:
    config = json.load(config_file)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['195.20.241.28', 'ecb613e.online-server.cloud', 'tbgeocon.com']
CSRF_TRUSTED_ORIGINS=['https://tbgeocon.com', 'https://195.20.241.28']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'captcha',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tbgeocon.urls'

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

WSGI_APPLICATION = 'tbgeocon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
DEFAULT_FROM_EMAIL = 'Kontakt <contact@tbgeocon.com>'  # Name unter dem die E-Mail verschickt wird und die dazugehörige E-Mail-Adresse
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # SMTP-Backend
EMAIL_HOST = 'smtp.ionos.de'
EMAIL_PORT = 587 # oder 587 oder was immer der Port deines E-Mail-Providers ist
EMAIL_USE_TLS = True  # Verbindung benutzt TLS-Verschlüsselung
EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']

JAZZMIN_SETTINGS ={
"site_logo": "../media/public/favicon/favicon.ico",
"site_title": "TB Geocon Admin",
"copyright": "TB Geocon",
"welcome_sign": "Welcome to TB Geocon Admin",
"site_brand": "TB Geocon",
"icons":{
    "auth": "fas fa-users-cog",
    "auth.Group": "fas fa-users",
    "auth.user": "fas fa-user",
    "main.Logo": "fab fa-css3",
    "main.Section": "fas fa-list",
    "main.Sub_section": "fas fa-sitemap",
},
"custom_css": "backend.css",
"custom_links": {
    "main": [{
        "name": "Home",
        "url": "http://127.0.0.1:8000/",
        "icon": "fas fa-home",
    }]
},
"order_with_respect_to": ["main", "main.Section", "main.Sub_section", "main.Logo", "auth"],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cerulean",
}

# Recaptcha
RECAPTCHA_PUBLIC_KEY = '6LfRCy8mAAAAAJPesMMSEujcb7hY9OphZ6JKBKM8'
RECAPTCHA_PRIVATE_KEY = config['RECAPTCHA_PRIVATE_KEY']
RECAPTCHA_REQUIRED_SCORE = 0.85

