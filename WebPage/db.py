import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQL = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db',
            'USER': 'my_user',
            'PASSWORD': 'my_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
}