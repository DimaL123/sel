from .models import *
from django import forms


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
