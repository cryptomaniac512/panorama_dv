import os

import environ

env = environ.Env(DEBUG=(bool, False))  # set default values and casting
environ.Env.read_env()                   # reading .env file

DEBUG = env('DEBUG')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = env('SECRET_KEY', cast=str)

ALLOWED_HOSTS = [
    'panorama-dv.ru',
]


DATABASES = {
    'default': env.db(),
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',

    'froala_editor',

    'main',
    'panoramas',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.get_portfolio',
                'main.context_processors.get_feedback_form',
            ],
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'panoramas.template_loaders.Loader',
            ),
        },
    },
]


def auth_validator(clsname) -> str:
    return f'django.contrib.auth.password_validation.{clsname}'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': auth_validator('UserAttributeSimilarityValidator')},
    {'NAME': auth_validator('MinimumLengthValidator')},
    {'NAME': auth_validator('CommonPasswordValidator')},
    {'NAME': auth_validator('NumericPasswordValidator')},
]


LANGUAGE_CODE = 'ru_ru'
TIME_ZONE = 'Asia/Vladivostok'
USE_I18N = True
USE_L10N = True
USE_TZ = True


MEDIA_ROOT = env(
    'MEDIA_ROOT', cast=str, default=os.path.join(BASE_DIR, 'media'),
)
MEDIA_URL = '/media/'

STATIC_ROOT = env(
    'STATIC_ROOT', cast=str, default=os.path.join(BASE_DIR, 'static'),
)
STATIC_URL = '/static/'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' if DEBUG \
    else 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', cast=str, default=None)
EMAIL_PORT = env('EMAIL_PORT', cast=int, default=None)
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', cast=str, default=None)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', cast=str, default=None)
EMAIL_FROM = env('EMAIL_FROM', cast=str, default=None)
EMAIL_TO = [EMAIL_FROM]


ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
