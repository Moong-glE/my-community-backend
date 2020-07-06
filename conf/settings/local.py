from .base import *

DEBUG = False

SECRET_KEY = "s*7%h87r6%8h6#p0q9&u&(eli*t=hl7c^zhsx*47n4=g(z9q=-"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mycommunity",
        "USER": "user",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

ALLOWED_HOSTS = ["*"]

STATIC_URL = "/static/"

CORS_ORIGIN_WHITELIST = ("localhost:3000/",)
