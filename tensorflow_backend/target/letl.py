LOCAL = False
if LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'tensorflow',
            'USER': 'root',
            'PASSWORD': 'mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'tensorflow',
            'USER': 'root',
            'PASSWORD': 'chungtoila',
            'HOST': '35.198.221.215',
            'PORT': '3306',
        }
    }

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True