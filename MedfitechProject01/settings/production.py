from MedfitechProject01.settings.base import *

DEBUG = False



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'medfitech_db',
        'USER': 'medfitech',
        'PASSWORD': 'parola123',
        'HOST': 'localhost',
        'PORT': '',

    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
