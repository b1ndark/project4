from django import forms
from .models import UserContact
from typerforum.models import CAR_MODELS
from django.db import models


class ContactForm(forms.ModelForm):
    """
    To display the Contact form
    """
    car_model = models.CharField(
        max_length=30, choices=CAR_MODELS, default="Select Car Model")

    class Meta:
        model = UserContact
        fields = ['name', 'email', 'car_model', 'subject', 'message_content']

        labels = {
            'name': 'Name',
            'email': 'Email',
            'car_model': 'Car Model',
            'subject': 'Subject',
            'message_content': 'Message'
        }
