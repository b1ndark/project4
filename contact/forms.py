from django import forms
from .models import UserContact
from django.db import models


class ContactForm(forms.ModelForm):
    """
    To display the Contact form
    """

    class Meta:
        model = UserContact
        fields = ['name', 'email', 'subject', 'message']

        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message'
        }
