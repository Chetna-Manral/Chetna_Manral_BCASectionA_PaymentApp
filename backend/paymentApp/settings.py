from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.auth',  
    'django.contrib.contenttypes',
    'rest_framework',
    'rest_framework.authtoken',
    'paymentApp',
]

ROOT_URLCONF = 'paymentApp.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = '7u5pum&*vqi_$(w-a$d07d$z_2jzcjc+j$hef!)xj9lse+fr=b'

STRIPE_SECRET_KEY = '7u5pum&*vqi_$(w-a$d07d$z_2jzcjc+j$hef!)xj9lse+fr=b'        # secret stripe key