# dev环境
from settings.base import *
# DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aisailing',
        'HOST': '192.168.12.161',
        'PORT': 3306,
        'USER': 'aisailing_rw',
        'PASSWORD': 'Udag_dy78',
    }
}