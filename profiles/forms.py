from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['car_model', 'city',
                  'county', 'country', 'postcode']

        labels = {
            'car_model': 'Car Model',
            'city': 'City',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Postcode'
        }


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
