import os
# import dj_database_url
#
# DB_NAME = os.environ.get('DB_NAME')
# DB_USER = os.environ.get('DB_USER')
# DB_PASSWORD = os.environ.get('DB_PASSWORD')
# DB_HOST = os.environ.get('DB_HOST')
# DB_PORT = os.environ.get('DB_PORT')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*')

DEBUG = False

ALLOWED_HOSTS = [ALLOWED_HOSTS]

# DATABASES = {'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': DB_NAME,
#     'USER': DB_USER,
#     'PASSWORD': DB_PASSWORD,
#     'HOST': DB_HOST,
#     'PORT': DB_PORT,
# }}
#
# DATABASE_URL = os.environ.get('DATABASE_URL')
# db_config = dj_database_url.config(default=DATABASE_URL, conn_max_age=600, conn_health_checks=True)
# DATABASES['default'].update(db_config)
