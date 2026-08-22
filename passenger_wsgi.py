import os
import sys

sys.path.insert(0, "/home/azamxwhg/football")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

from config.wsgi import application
