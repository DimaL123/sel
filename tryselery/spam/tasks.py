from django.core.mail import send_mail
from tryselery.celery import app
from .models import *
from .srvise import send


@app.task
def send_spam(user_email):
    send(user_email)


@app.task
def send_spam_2():
    for i in Contacts.objects.all():
        send_mail("Spam", 'Spam!!', 'd9285765@gmail.com', [i.email], fail_silently=False)