from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    ACCOUNT_DEFAULT_HTTP_PROTOCOL=(str, "https"),
    EMAIL_BACKEND="FIXME LATER",
)
env.read_env(str(BASE_DIR / "project/.env"))
