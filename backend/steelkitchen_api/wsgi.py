import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'steelkitchen_api.settings')

django.setup()
from django.core.management import call_command
try:
    call_command('collectstatic', '--noinput', verbosity=0)
except Exception as e:
    print(f"collectstatic failed: {e}")

application = get_wsgi_application()
app = application