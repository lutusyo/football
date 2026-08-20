#config/settings/production.py

from decouple import config

from .base import *

DEBUG = False

ALLOWED_HOSTS = config("ALLOWED_HOSTS",
    cast=lambda value: [host.strip() for host in value.split(",")])

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",default="",
    cast=lambda value: [origin.strip() for origin in value.split(",") if origin.strip()]
    )

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
