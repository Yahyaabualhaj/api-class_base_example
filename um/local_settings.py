# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3m*ba-5hvdt@n(whd9#_ek=jw=noxir5!f1=4i18*57&anop5m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['142.93.140.140']

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
