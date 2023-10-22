from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['car_model', 'city', 'county', 'country', 'postcode']

        labels = {
            'car_model': 'Car Model',
            'city': 'City',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Postcode'
        }
