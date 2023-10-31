from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from typerforum.models import CAR_MODELS
from django_countries.fields import CountryField


class ProfileForm(forms.ModelForm):
    """
    To display the Profile form
    """

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
    """
    To display the Signup form
    """

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    """
    To display the Edit Profile form
    """

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    city = forms.CharField(required=True)
    county = forms.CharField(required=False)
    country = CountryField(blank_label='Select country')
    postcode = forms.CharField(required=False)
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'city', 'county', 'postcode']
