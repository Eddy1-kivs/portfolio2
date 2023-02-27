from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = SendAMessage
        fields = ['name', 'email', 'subject', 'message']
