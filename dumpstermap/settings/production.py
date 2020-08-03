import dj_database_url

# Keep this import!
# noinspection PyUnresolvedReferences
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dumpstermap.org',
                 'dumpstermap.vercel.app',
                 'dumpstermap.herokuapp.com']

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = [
#     'dumpstermap.vercel.app',
#     'http://localhost:4200/'
# ]

STATIC_URL = '/static/'

DATABASES = {
    # Retrieve database settings from env variable DATABASE_URL
    'default': dj_database_url.config(engine='django.contrib.gis.db.backends.postgis')
}
