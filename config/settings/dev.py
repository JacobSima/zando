from .base                              import *


DEBUG  = not bool(config["DEBUG"])

IS_ENV = 'DEV'

ALLOWED_HOSTS = [
    'btk.zigida.systems',
    'localhost',
    '127.0.0.1',
]


INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql',
        'NAME'      : config["ZG_DB_NAME"][0],
        'USER'      : config["ZG_DB_USER"],
        'PASSWORD'  : config["ZG_DB_PASSWORD"],
        'HOST'      : config["ZG_DB_HOST"],
        'PORT'      : config["ZG_DB_PORT"],
    }
}


# DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS'   : False,
    'SHOW_TOOLBAR_CALLBACK' : show_toolbar,
}


ZIG_USER_DIR = {
    "media" : f"{ZIGIDA_DIR}/media"
}

EMAIL_BACKEND   = config["EMAIL_BACKEND"]
EMAIL_HOST      = config["EMAIL_HOST"]
EMAIL_USE_TLS   = bool(config["DEBUG"])
EMAIL_PORT      = config["EMAIL_PORT"]
EMAIL_SENDER    = config["EMAIL_SENDER"]
EMAIL_PASSWORD  = config["EMAIL_PASSWORD"]

EMAIL_ISSUE_SENDER    = config["EMAIL_ISSUE_SENDER"]
EMAIL_ISSUE_RECEIVER  = config["EMAIL_ISSUE_RECEIVER"]
EMAIL_ISSUE_PASSWORD  = config["EMAIL_ISSUE_PASSWORD"]

SENDSMS_BACKEND = 'sendsms.backends.console.SmsBackend'


# OVERRIDE THE REMOTE HOST WITH LOCAL HOST
# DATABASES['default']['HOST'] = 'localhost'


print("\n")
print("DEBUG        = ", DEBUG)
print("MODE         = ", IS_ENV)
print("DATABASES    = ", DATABASES['default']['NAME'])
print("HOST         = ", DATABASES['default']['HOST'])
print("TEMPLATES    = ", TEMPLATES[0]['DIRS'])
# print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT)
print("\n")
