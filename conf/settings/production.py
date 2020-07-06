from .base import *

import configparser
import sys

DEBUG = False

DATABASES = {
    "default": {"ENGINE": "django.db.backends.postgresql", "NAME": "mycommunity",}
}

ALLOWED_HOSTS = ["localhost"]

STATIC_URL = "/static/"

CORS_ORIGIN_WHITELIST = ("localhost:3000/",)

config = configparser.ConfigParser()
config.read("././config.ini")

for key, value in config["production"].items():
    setattr(sys.modules[__name__], key, value)
