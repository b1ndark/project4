from django import forms
from .models import UserContact


class ContactForm(forms.ModelForm):
    """
    To display the Contact form
    """

    class Meta:
        model = UserContact
        fields = ['name', 'email', 'car_model', 'subject', 'message_content']

        labels = {
            'name': 'Name',
            'email': 'Email',
            'car_model': 'Car Model',
            'subject': 'Subject',
            'message_content': 'Content of the message'
        }
