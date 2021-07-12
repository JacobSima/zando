import os, json
from sys                                    import platform
from pathlib                                import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


BASE_DIR = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                )
            )

ZIGIDA_DIR     = '//localhost/zigida'

if platform == "linux" or platform == "linux2":
    # linux
    PLATFORM = "linux"

    with open("/etc/config.json") as config_file:
        config = json.load(config_file)

if platform == "darwin":
    # OS X
    PLATFORM = "darwin"

    with open(f"{ZIGIDA_DIR}/config.json") as config_file:
        config = json.load(config_file)

if platform == "win32":
    # Windows...
    PLATFORM = "win32"

    with open(f"{ZIGIDA_DIR}/config.json") as config_file:
        config = json.load(config_file)

#print("CONFIG = ", config)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config["SECRET_KEY"]
# Application definition

AUTH_USER_MODEL = 'sr_users.SRUser'

AUTHENTICATION_BACKENDS = ('config.backends.AuthBackend',)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # API - Apps
    'rest_framework',
    'rest_framework.authtoken',

    # Third Party Apps
    'django_countries',
    'crispy_forms',
    'bootstrap4',
    'django_user_agents',
    'django_extensions',

    # PROJECTS' APPS -- BELOW

    # ACCOUNTING APPS
    'zigida.apps.db.accounting.banks',
    'zigida.apps.db.accounting.coupons',
    'zigida.apps.db.accounting.items',
    'zigida.apps.db.accounting.orders',
    'zigida.apps.db.accounting.payments',
    'zigida.apps.db.accounting.receipts',
    'zigida.apps.db.accounting.refunds',
    'zigida.apps.db.accounting.vouchers',

    # COMMUNICATION APPS
    'zigida.apps.db.communications.emails',

    # PRODUCTS APPS
    'zigida.apps.db.products.categories',
    'zigida.apps.db.products.colors',
    'zigida.apps.db.products.products',
    'zigida.apps.db.products.sizes',

    # STORES APPS
    'zigida.apps.db.stores.openinghours',
    'zigida.apps.db.stores.stores',

    # GENERAL - PUBLIC APPS
    'zigida.apps.db.addresses',
    'zigida.apps.db.customers',
    'zigida.apps.db.locations',
    'zigida.apps.db.sr_issues',
    'zigida.apps.db.sr_users',
    'zigida.apps.db.visitors',

    'zigida.templates',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'zigida/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# DRF Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}


LOGIN_REDIRECT_URL = '/login/'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE   = 'en-us'

TIME_ZONE       = 'Africa/Kinshasa'

USE_I18N        = True

USE_L10N        = True

USE_TZ          = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
BASE_PATH = os.path.join(BASE_DIR)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_PATH, 'zigida/static')

MEDIA_URL   = '/media/'
MEDIA_ROOT  = os.path.join(BASE_PATH, f"{ZIGIDA_DIR}")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Models Graph settings
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
