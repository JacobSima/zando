from . base                                     import *


DEBUG = bool(config["DEBUG"])

IS_ENV = 'PROD'

ALLOWED_HOSTS = config["ALLOWED_HOSTS"]


# DATABASES['default'] =  dj_database_url.config()
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

# MIDDLEWARE += [
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

EMAIL_BACKEND   = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST      = config["EMAIL_HOST"]
EMAIL_USE_TLS   = bool(config["EMAIL_USE_TLS"])
EMAIL_PORT      = config["EMAIL_PORT"]
EMAIL_SENDER    = config["EMAIL_SENDER"]
EMAIL_PASSWORD  = config["EMAIL_PASSWORD"]

EMAIL_ISSUE_SENDER    = config["EMAIL_ISSUE_SENDER"]
EMAIL_ISSUE_RECEIVER  = config["EMAIL_ISSUE_RECEIVER"]
EMAIL_ISSUE_PASSWORD  = config["EMAIL_ISSUE_PASSWORD"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#STATIC_ROOT  =   os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'
if PLATFORM == "win32":
    config['ZIGIDA_DIR'] = ZIGIDA_DIR

MEDIA_ROOT = os.path.join(BASE_PATH, f"{config['ZIGIDA_DIR']}")

# Extra lookup directories for collectstatic to find static files
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

#  Add configuration for static files storage using whitenoise
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# prod_db  =  DATABASES.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)

print("\n")
print("DEBUG        = ", DEBUG)
print("MODE         = ", IS_ENV)
print("PLATFORM     = ", PLATFORM)
# print("DATABASES    = ", DATABASES['default'])
print("DB_HOST      = ", DATABASES['default']['HOST'])
# print("ALLOWED_HOSTS   = ", ALLOWED_HOSTS)
# print("TEMPLATES    = ", TEMPLATES[0]['DIRS'])
# print("STATIC_ROOT  = ", STATIC_ROOT)
# print("MEDIA_ROOT   = ", MEDIA_ROOT)
print("\n")
