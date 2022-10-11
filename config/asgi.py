"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# import dotenv # django-dotenv
from dotenv import load_dotenv  # python-dotenv

# dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')) # django-dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))  # python-dotenv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
