from .base import *

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_USE_TLS = env("EMAIL_PORT")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = 'info@real-estate.com'
# EMAIL_HOST= env("EMAIL_HOST")
# EMAIL_HOST_USER= env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD= env("EMAIL_HOST_PASSWORD")
# EMAIL_PORT= env("EMAIL_PORT")
# DOMAIN = env("DOMAIN")
# SITE_NAME = "Real Estate"

# .env file content:
# ----------------------------
# EMAIL_HOST=sandbox.smtp.mailtrap.io
# EMAIL_HOST_USER=e61f02d9f7d37a
# EMAIL_HOST_PASSWORD=62c3421c12973c
# EMAIL_PORT=2525
# DOMAIN=localhost:8000


DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}

# CELERY_BROKER_URL = env("CELERY_BROKER")
# CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
# CELERY_TIMEZONE = "UTC"