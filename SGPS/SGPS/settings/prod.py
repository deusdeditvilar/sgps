from .base import *

DEBUG = False

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': os.environ.get('DB_NAME', 'postgres'),
         'USER': os.environ.get('DB_USER', 'root'),
         'PASSWORD': os.environ.get('DB_PASS', 'senhadobanco'),
         'HOST': 'programas-socias-db.cqaxnjleyjy2.us-east-1.rds.amazonaws.com',
         'PORT': '5432',
    }
}