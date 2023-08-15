import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tryselery.settings')
app = Celery('tryselery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



app.conf.beat_schedule={
    'send-spam':{
        'task':'spam.tasks.send_spam_2',
        'schedule':crontab(minute='*/1')
    }
}