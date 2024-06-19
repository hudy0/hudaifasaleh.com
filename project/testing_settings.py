from .settings import *  # noqa

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# An in-memory database should be good enough for now.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
