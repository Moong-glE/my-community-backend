from .base import *

DEBUG = True

SECRET_KEY = "s*7%h87r6%8h6#p0q9&u&(eli*t=hl7c^zhsx*47n4=g(z9q=-"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

ALLOWED_HOSTS = ["*"]

STATIC_URL = "/static/"
