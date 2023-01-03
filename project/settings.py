import os
import environs
# from dotenv import load_dotenv
# load_dotenv()
from environs import Env
env=Env()
env.read_env()

DATABASES = {
    'default': {
        "ENGINE": env("ENGINE"),
        "HOST": env("HOST"),
        "PORT": env("PORT"),
        "NAME": env("NAME"),
        "USER": env("USER"),
        "PASSWORD": env("PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("debug")

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-RU'

DATETIME_FORMAT = 'd B Y H m'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
