"""
Django settings for laborapp project.
Generated by 'django-admin startproject' using Django 2.2.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

#import pymysql#para entornos de desarrollo en ubuntu
#import django_heroku  # para producción
#pymysql.install_as_MySQLdb()##para entornos de desarrollo en ubuntu

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_a4olqm7h!k+$04mbl&*(duyj&&!a5(8f=c^fht@s^3776+n1)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user_profile',
    'rest_framework.authtoken',# danger....is very important make a migration and dont use Token of this library before that installed
    'persona',
    'corsheaders',
    'consultorioJuridico',
    'persona_natural',
    'empresa',
    'contratoLaboral',
    'demandaPersonaNatural',
    'archivoDemanda',
    'demandaEmpresa',
    'conflictoDespidoSJC',
    'conflictoPagoSalario',
    'conflictoVacaciones',
    'conflictoCesantias',
    'conflictoLiquidacion',
    'conflictoContactaAbogado',
    'conflictoPrimas',
    'conflictoInteresesCesantias'
]
MIDDLEWARE = [


    'corsheaders.middleware.CorsMiddleware',#cors producción
    'django.middleware.common.CommonMiddleware', #cors producción
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # **cors......
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = 'laborapp.urls'

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

WSGI_APPLICATION = 'laborapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

"""
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ingnova1_laborapp',
        'USER': 'ingnova1_stiven',
        'PASSWORD': '#Stiven1911',
        'HOST': '199.79.62.144',
        'PORT': '3306',
    }


    'default': {
    'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ingnova1_prueba',
        'USER': 'ingnova1_stiven',
        'PASSWORD': '#Stiven1911',
        'HOST': '199.79.62.144',
        'PORT': '3306',

        }


    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'laborapp',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',

    }

         'default': {
            'ENGINE': 'mysql_cymysql',
            'NAME': 'ingnova1_laborapp',
            'USER': 'ingnova1_stiven',
            'PASSWORD': '#Stiven1911',
            'HOST': '199.79.62.144',
            'PORT': '3306',

        }

"""

DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'ingnova1_laborapp',
             'USER': 'ingnova1_stiven',
             'PASSWORD': '#Stiven1911',
             'HOST': '199.79.62.144',
             'PORT': '3306',

             }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
AUTH_USER_MODEL = 'user_profile.UserProfile'


#Para entornos de desarrollo*******



CORS_ORIGIN_ALLOW_ALL = True


#para entornos de desarollo******


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')#para producción
""" la anterior linea fue adicionaeda debido al error que se mostraba en HEROKU"""
