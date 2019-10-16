# SECURITY WARNING: keep the secret key used in production secret!
import os

from um.settings import BASE_DIR

SECRET_KEY = '3m*ba-5hvdt@n(whd9#_ek=jw=noxir5!f1=4i18*57&anop5m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['178.62.240.64','falconsroad.com', 'www.falconsroad.com']
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'um_prod',
        'USER': 'dbadmin',
        'PASSWORD': 'asdasdasd',
        'HOST': 'localhost',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
