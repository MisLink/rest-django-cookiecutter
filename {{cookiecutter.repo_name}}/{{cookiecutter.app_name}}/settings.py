import re

from django.utils.log import DEFAULT_LOGGING
import environ

root = environ.Path(__file__) - 2

environ.Env.read_env(root(".env"))

env = environ.Env(DEBUG=(bool, False))

# core
DEBUG = env("DEBUG")
ADMINS = [x.split(":") for x in env.list("ADMINS")]
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
APPEND_SLASH = False
CACHES = {"default": env.cache()}
DATABASES = {"default": env.db()}
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024
DISALLOWED_USER_AGENTS = [
    re.compile(x) for x in env.list("DISALLOWED_USER_AGENTS", default=[])
]
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "{{cookiecutter.app_name}}.users.apps.Config",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
LOGGING = DEFAULT_LOGGING
ROOT_URLCONF = "{{cookiecutter.app_name}}.urls"
SECRET_KEY = env("SECRET_KEY")
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
LANGUAGE_CODE = "zh-Hans"
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = "{{cookiecutter.app_name}}.wsgi.application"

# auth
AUTH_USER_MODEL = "users.User"
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa B950
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# session

# static
STATIC_URL = "/static/"

# celery
CELERY_BROKER_URL = env.url("CELERY_BROKER_URL")

# drf
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "DATE_FORMAT": "%Y-%m-%d",
    "DATE_INPUT_FORMATS": "%Y-%m-%d",
    "TIME_FORMAT": "%H:%M:%S",
    "TIME_INPUT_FORMATS": "%H:%M:%S",
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DATETIME_INPUT_FORMATS": "%Y-%m-%d %H:%M:%S",
}
