import os
from pathlib import Path
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 's3cr3t_k3y')

DEBUG = True  # Ustaw na False w środowisku produkcyjnym

ALLOWED_HOSTS = ['*']  # Zmień na domenę swojej aplikacji w produkcji

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',  # Nasza aplikacja
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  # Można wyłączyć na potrzeby testów
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chatbot_therapist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # W razie potrzeby
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

WSGI_APPLICATION = 'chatbot_therapist.wsgi.application'

# Baza danych
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Zmień na np. postgresql dla produkcji
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Walidacja haseł
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # Dodaj kolejne walidatory w razie potrzeby
]

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Pliki statyczne
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# E-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.example.com')
EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

# Dodatkowe ustawienia
SESSION_COOKIE_AGE = 1209600  # 2 tygodnie
SESSION_SAVE_EVERY_REQUEST = True