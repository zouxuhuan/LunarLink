"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os
import sys

from loguru import logger

from conf.env import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, "extra_apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^v68x$m2x($7!z@8lt548otbgev)@on&tntu3qts^s2z3xx(_a"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = locals().get("DEBUG", True)
ALLOWED_HOSTS = locals().get("ALLOWED_HOSTS", ["*"])

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Application definition

INSTALLED_APPS = [
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "drf_yasg",
    "django_celery_beat",
    "django_celery_results",
    "lunaruser",
    "lunarlink",
]

MIDDLEWARE = [
    "backend.utils.middleware.PerformanceAndExceptionLoggerMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "log_request_id.middleware.RequestIDMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "backend.utils.middleware.VisitTimesMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "./templates")],
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

ASGI_APPLICATION = "backend.asgi.application"
WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": DATABASE_NAME,
        "USER": DATABASE_USER,
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": DATABASE_HOST,
        "PORT": DATABASE_PORT,
        "OPTIONS": {
            "charset": "utf8mb4",  # 设置字符集为utf8mb4
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "zh-Hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = False

# ================================================= #
# *************** REST_FRAMEWORK配置 *************** #
# ================================================= #
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "backend.utils.auth.MyJWTAuthentication",  # 设置全局的默认身份验证方案
    ],
    "UNAUTHENTICATED_USER": None,
    "UNAUTHENTICATED_TOKEN": None,
    # json form 渲染
    # 设置全局默认的解析器集
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",  # 解析 JSON 请求内容
        "rest_framework.parsers.FormParser",  # 解析 HTML 表单内容
        "rest_framework.parsers.MultiPartParser",  # 解析多部分HTML表单内容，支持文件上传
        "rest_framework.parsers.FileUploadParser",  # 解析原始文件上传内容
    ],
    "DEFAULT_PAGINATION_CLASS": "backend.utils.pagination.MyPageNumberPagination",  # 默认分页器
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",  # 有经过身份认证确定用户身份才能访问
    ),
}

# ================================================= #
# ****************** simplejwt配置 ***************** #
# ================================================= #
JWT_AUTH = {
    "JWT_EXPIRATION_DELTA": datetime.timedelta(days=1),
    "JWT_ALLOW_REFRESH": True,
}

AUTH_USER_MODEL = "lunaruser.MyUser"

# ====================================#
# ****************swagger************#
# ====================================#
SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": "backend.utils.swagger.CustomSwaggerAutoSchema",
    "SECURITY_DEFINITIONS": {
        "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
    # 接口文档中方法列表以首字母升序排列
    "APIS_SORTER": "alpha",
    # 如果支持json提交, 则接口文档中包含json输入框
    "JSON_EDITOR": True,
    # 方法列表字母排序
    "OPERATIONS_SORTER": "alpha",
    "VALIDATOR_URL": None,
    "USE_SESSION_AUTH": False,
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/django_static/"

# 指定static文件的路径，缺少这个配置，collectstatic无法加载extent.js
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# collectstatic 之后的文件存放路径
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

for level in ["INFO", "WARNING", "ERROR"]:
    logger.add(
        f"logs/{level.lower()}.log",
        format="{time:YYYY-MM-DD HH:mm:ss.SSS}"
        " [pid:{process} -> thread:{thread.name}]"
        " {level}"
        " [{name}:{function}:{line}]"
        " {message}",
        level=level,
        rotation="00:00",
        retention="14 days",
    )

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "%(levelname)-2s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "color": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(green)s%(asctime)s [%(request_id)s] %(name)s %(log_color)s%(levelname)s [pid:%(process)d] "
            "[%(filename)s->%(funcName)s:%(lineno)s] %(cyan)s%(message)s",
            "log_colors": {
                "DEBUG": "black",
                "INFO": "white",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        }
        # 日志格式
    },
    "filters": {
        "request_id": {"()": "log_request_id.filters.RequestIDFilter"},
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",  # 过滤器，只有当setting的DEBUG = True时生效
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
        "default": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/info.log"),
            "maxBytes": 1024 * 1024 * 50,
            "backupCount": 5,
            "formatter": "color",
            "filters": ["request_id"],
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "color",
            "filters": ["request_id"],
        },
    },
    "loggers": {
        "django": {
            "handlers": ["default", "console"],
            "level": "INFO",
            "propagate": True,
        },
        "lunarlink": {
            "handlers": ["default", "console"],
            "level": "INFO",
            "propagate": True,
        },
        "httprunner": {
            "handlers": ["default", "console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# celery 配置
CELERY_BROKER_URL = MQ_URL  # 消息队列地址
CELERY_RESULT_BACKEND = "django-db"  # celery结果存储到数据库中
CELERY_TIMEZONE = TIME_ZONE  # celery 时区问题
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"  # Backend数据库
DJANGO_CELERY_BEAT_TZ_AWARE = False  # 时区设置
CELERY_ENABLE_UTC = False  # 时区设置

# 设置请求体的最大大小
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50M


LOG_REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"
GENERATE_REQUEST_ID_IF_NOT_IN_HEADER = True
REQUEST_ID_RESPONSE_HEADER = "RESPONSE_HEADER_NAME"

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = []

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
    "VIEW",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "Project",
)
