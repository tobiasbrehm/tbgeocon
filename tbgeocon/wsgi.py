"""
WSGI config for tbgeocon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import site

sys.path.append("/home/webmaster/tbgeocon")
site.addsitedir("/home/webmaster/tbgeocon/venv/lib/python3.8/site-packages")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbgeocon.settings')

application = get_wsgi_application()
