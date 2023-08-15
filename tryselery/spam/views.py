from django.shortcuts import render
from django.db import models
from django.views.generic import CreateView
from .models import Contacts
from .forms import ContactsForm
from .tasks import send_spam
from .srvise import send


class ContactsViev(CreateView):
    model = Contacts
    form_class = ContactsForm
    success_url = "/"
    template_name = "spam/Contacts.html"

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam.delay(form.instance.email)
        return super().form_valid(form)
