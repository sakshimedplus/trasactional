import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transatioional_webhook.settings')

# Create the Celery app
app = Celery('transatioional_webhook')

# Load configuration from Django settings using namespace CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all registered Django apps
app.autodiscover_tasks()