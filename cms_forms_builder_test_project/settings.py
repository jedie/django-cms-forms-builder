
import logging
import os

import django

from django_tools.settings_utils import FnMatchIps

DIRNAME = os.path.dirname(__file__)

DEBUG = True

# Required for the debug toolbar to be displayed:
INTERNAL_IPS = FnMatchIps(["localhost", "127.0.0.1", "::1", "172.*.*.*", "192.168.*.*", "10.0.*.*"])


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.abspath(DIRNAME), "test_database.sqlite3")
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites', # django-cms will import sites models

    'cms', # https://github.com/divio/django-cms
    'menus', # django-cms will import menu models
    'treebeard', # https://github.com/django-treebeard/django-treebeard
    'sekizai', # https://github.com/ojii/django-sekizai

    'django_tools', # https://github.com/jedie/django-tools/
    'django_cms_tools', # https://github.com/jedie/django-cms-tools/

    'debug_toolbar', # https://github.com/jazzband/django-debug-toolbar/

    # Important: 'cms_forms_builder' must be inserted *before* 'forms_builder.forms'

    'cms_forms_builder',
    'cms_forms_builder_test_project.test_app',

    'forms_builder.forms', # https://github.com/stephenmcd/django-forms-builder
)

ROOT_URLCONF = 'cms_forms_builder_test_project.urls'

SITE_ID=1

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.abspath(DIRNAME), "static")

# don't load jquery from ajax.googleapis.com, just use django's version:
# https://django-debug-toolbar.readthedocs.io/en/stable/configuration.html#debug-toolbar-config
from debug_toolbar.settings import CONFIG_DEFAULTS as DEBUG_TOOLBAR_CONFIG
DEBUG_TOOLBAR_CONFIG["JQUERY_URL"] = "/static/admin/js/vendor/jquery/jquery.min.js"

SECRET_KEY = 'This is not secret, but this is only a test project ;)'

ALLOWED_HOSTS=["*"]
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.abspath(DIRNAME), "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',

                'cms_forms_builder_test_project.test_app.context_processors.debug_info'
            ],
        },
    },
]

USE_TZ = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-LANGUAGE_CODE
LANGUAGE_CODE = "en"

# http://docs.django-cms.org/en/latest/reference/configuration.html#std:setting-CMS_LANGUAGES
CMS_LANGUAGES = {
    1: [
        {
            "code": "de",
            "fallbacks": ["en"],
            "hide_untranslated": False,
            "name": "German",
            "public": True,
            "redirect_on_fallback": False,
        },
        {
            "code": "en",
            "fallbacks": ["de"],
            "hide_untranslated": False,
            "name": "English",
            "public": True,
            "redirect_on_fallback": False,
        },
    ],
    "default": { # all SITE_ID"s
        "fallbacks": [LANGUAGE_CODE],
        "redirect_on_fallback": False,
        "public": True,
        "hide_untranslated": False,
    },
}

# https://docs.djangoproject.com/en/1.8/ref/settings/#languages
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGES = tuple([(d["code"], d["name"]) for d in CMS_LANGUAGES[1]])

# # http://django-parler.readthedocs.org/en/latest/quickstart.html#configuration
# PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
# PARLER_LANGUAGES = CMS_LANGUAGES

# http://docs.django-cms.org/en/latest/topics/permissions.html
CMS_PERMISSION=False


CMS_TEMPLATES = (
    ("cms/base.html", "Basic CMS Template"),
)

CMS_PLACEHOLDER_CONF = {
    "content": {
        # "plugins": ["PlainTextPlugin"],
        # "default_plugins": [
        #     {
        #         "plugin_type": "PlainTextPlugin",
        #         "values": {"text": "(Default content)"},
        #     },
        # ],
    },
}

#_____________________________________________________________________________
# cut 'pathname' in log output

try:
    old_factory = logging.getLogRecordFactory()
except AttributeError: # e.g.: Python < v3.2
    pass
else:
    def cut_path(pathname, max_length):
        if len(pathname)<=max_length:
            return pathname
        return "...%s" % pathname[-(max_length-3):]

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.pathname = cut_path(record.pathname, 30)
        return record

    logging.setLogRecordFactory(record_factory)


#-----------------------------------------------------------------------------

# tip to get all existing logger names:
#
# ./manage.py shell
#
# import logging;print("\n".join(sorted(logging.Logger.manager.loggerDict.keys())))
#
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)8s %(pathname)s:%(lineno)-3s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {'class': 'logging.NullHandler',},
        'console': {
            'class': 'logging.StreamHandler',
            # 'formatter': 'simple'
            'formatter': 'verbose'
        },
    },
    'loggers': {
        "": {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        "cms_forms_builder": {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        "cms_forms_builder_test_project": {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        "django_tools": {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        "django_cms_tools": {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
