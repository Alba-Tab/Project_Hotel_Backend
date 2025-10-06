from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-dhl8e*%m-d7-9(7m1v=+@eo1!qudi)%+p^og@!whyw68ap)f0)'

DEBUG = True

ALLOWED_HOSTS = []

# aplicacioness definidas para el esquema publico
SHARED_APPS = [
    "django_tenants",
    "customers",
    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    "rest_framework",
]
TENANT_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.auth', #necesario para el modelo de usuario personalizado por esquema
    "apps.usuarios",
    'django.contrib.admin',
    'rest_framework.authtoken',
    "core",
    "apps.reservas",
    "apps.habitaciones",
    "apps.finanzas",
]

INSTALLED_APPS = list(SHARED_APPS) + [a for a in TENANT_APPS if a not in SHARED_APPS]

TENANT_MODEL = "customers.Client"
TENANT_DOMAIN_MODEL = "customers.Domain"
# Esquema publico default donde se guarda las configuraciones globales y shared aplicaciones
PUBLIC_SCHEMA_NAME = "public"
TENANT_URLCONF = "cadena_hoteleria.urls_tenant"
PUBLIC_SCHEMA_URLCONF = "cadena_hoteleria.urls_public"
                        #hotel_prueba.localhost

AUTH_USER_MODEL = "usuarios.Usuario"
MIDDLEWARE = [
    "django_tenants.middleware.main.TenantMainMiddleware", 
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'cadena_hoteleria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cadena_hoteleria.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": 'django_tenants.postgresql_backend',
        #"ENGINE": 'django.db.backends.postgresql',
        "NAME": "hotel_db",
        "USER": "postgres", 
        "PASSWORD": "1234", # Cambia esto por tu password real
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
DATABASE_ROUTERS = [
    'django_tenants.routers.TenantSyncRouter',
]

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
