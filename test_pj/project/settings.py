"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-u##hmh@lc!$f#qkfc+r!%5_7shs!m1k68c8#n2^y=9(^ok#s4@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "notify"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


####################### 로깅에 대한 설정 #######################
# LOGGING = {
#     # logging 모듈 version
#     'version': 1,
#     # 기존의 설정된 로거들을 사용하지 않는 것에 대한 유무
#     'disable_existing_loggers': False,
#     # filters : 특정 조건에서 로그를 출력하거나 출력하지 않기 위해서 사용
#     # formatters : 로그를 출력할 형식을 정의
#     # handlers : 로그의 출력 방법 정의
#     'handlers': {
#         # 콘솔에 로그 출력
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#         # 파일로 로그를 남김
#         'file': {
#             'class': 'logging.FileHandler',
#             # 로그의 파일 위치
#             'filename': './debug.log',
#         },
#         # python manage.py runserver로 작동하는 개발서버에서만 사용하는 핸들러-콘솔에 로그 출력
#         'django.server': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'django.server',
#         },
#         # 로그 내용을 이메일로 전송하는 핸들러, ERROR이상 & DEBUG=FALSE일떄만 로그 전송
#         # 핸들러 사용 시 환경설정파일에 ADMINS라는 항목을 추가하고 관리자 이메일 등록필요
#         # 이메일 발송을 위한 SMTP 설정도 필요
#         # 'mail_admins': {
#         #     'level': 'ERROR',
#         #     'filters': ['require_debug_false'],
#         #     'class': 'django.utils.log.AdminEmailHandler'
#         # }
#     },
#     # 로그를 출력하는 프로그램에서 사용하는 로거 이름
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#         },
#     },
# }
####################################################################