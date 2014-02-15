"""
Django settings for aist project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def rel(*args):
    return os.path.join(BASE_DIR, *args)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd(zk)-3&znv*&hx&&6a@)=s*wo#f_#u_u85oxv!17%a&+aj#(q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['aist-sm.ru', 'www.aist-sm.ru']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aist_app',
    'tinymce',
    'captcha'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aist.urls'

WSGI_APPLICATION = 'aist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    rel('static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATIC_ROOT = rel('static_root')

TINYMCE_JS_URL = os.path.join(STATIC_URL, 'tiny_mce/tiny_mce.js')
TINYMCE_JS_ROOT =  os.path.join(rel('static'), 'tiny_mce') # change to static_root when deploying

TINYMCE_DEFAULT_CONFIG = {
    # 'plugins': "table,spellchecker,paste,searchreplace",
    "plugins": "safari",
    'theme': "advanced",
    'theme_advanced_resizing': True,
    'theme_advanced_resizing_min_height': 250,
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align': 'left', 
    'theme_advanced_buttons1' : "bold,italic,strikethrough,bullist,numlist," 
                            "separator,undo,redo,separator,link,unlink,image," 
                            "separator,cleanup,code,removeformat,charmap,"
                            "fullscreen,paste",
    'theme_advanced_buttons2' : "justifyleft,justifycenter,justifyright,justifyfull",
}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False

RECAPTCHA_PUBLIC_KEY = '6LePoe4SAAAAAIgPk25UVV-M0rFlxWc70Iephs57'
RECAPTCHA_PRIVATE_KEY = '6LePoe4SAAAAAAiZvmo4uV6LkMTDgqhatmwza9n1'

try:
    from settings_local import *
except ImportError:
    pass
