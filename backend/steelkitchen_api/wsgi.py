import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'steelkitchen_api.settings')

# Run collectstatic and migrate on cold start (Vercel serverless)
import django
django.setup()

from django.core.management import call_command
try:
    call_command('collectstatic', '--noinput', '--clear', verbosity=0)
    call_command('migrate', '--noinput', verbosity=0)
except Exception as e:
    print(f"Startup command failed: {e}")

application = get_wsgi_application()
app = application