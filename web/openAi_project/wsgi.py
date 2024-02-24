"""
WSGI config for openAi_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv
from django.core.wsgi import get_wsgi_application

CURRENT_DIR=pathlib.path(__file__).resolve().parent
BASE_DIR=CURRENT_DIR.parent
ENV_FILE_PATH=BASE_DIR /".env"

dotenv.read_dotenv(str(ENV_FILE_PATH))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openAi_project.settings')

application = get_wsgi_application()
