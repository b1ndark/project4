from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from typerforum.models import CAR_MODELS
from django_countries.fields import CountryField
from django.db import models


class ProfileForm(forms.ModelForm):
    """
    To display the Profile form
    """

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'car_model',
                  'city', 'county', 'country', 'postcode']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
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
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    """
    To display the Edit Profile form
    """

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    car_model = models.CharField(
        max_length=30, choices=CAR_MODELS, default="Select Car Model"
    )
    user_email = models.EmailField(default="email")
    city = forms.CharField(required=False)
    county = forms.CharField(required=False)
    country = CountryField(blank_label='Select Country')
    postcode = forms.CharField(required=False)
    password = None

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profile_image', 'user_email',
                  'car_model', 'city', 'county', 'country', 'postcode',
                  'facebook_url', 'twitter_url', 'instagram_url', 
                  'youtube_url']

        labels = {
            'facebook_url': 'Facebook',
            'twitter_url': 'Twitter',
            'instagram_url': 'Instagram',
            'youtube_url': 'Youtube'
        }
