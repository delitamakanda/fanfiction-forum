from config.settings import *
import os

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = os.environ['DEBUG']

hostname = os.environ['DBHOST']

# Configure Postgres database; the full username for PostgreSQL flexible server is
# username (not @sever-name).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS'] 
    }
}

# WhiteNoise configuration
MIDDLEWARE += [                                                                                       
    'whitenoise.middleware.WhiteNoiseMiddleware',                 
]

STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

# email 
DEFAULT_FROM_EMAIL = os.environ['ADMIN_EMAIL']
SERVER_EMAIL = os.environ['ADMIN_EMAIL']

ADMINS = [
  (os.environ['ADMIN_NAME'], os.environ['ADMIN_EMAIL']),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['SENDGRID_SERVER']
EMAIL_PORT = os.environ['SENDGRID_PORT']
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_TIMEOUT = 500