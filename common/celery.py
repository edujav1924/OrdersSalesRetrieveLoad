# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

#configuracion celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'common.settings')
app = Celery('common')

app.config_from_object('django.conf:settings', namespace='CELERY')

# obtiene todas las tareas
app.autodiscover_tasks()
