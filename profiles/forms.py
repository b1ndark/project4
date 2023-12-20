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

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}), required=False)
    car_model = models.CharField(
        max_length=30, choices=CAR_MODELS, default="Select Car Model"
    )
    email_address = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': '"typperforum@example.com"'}), required=False)
    city = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'City'}), required=False)
    county = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'County'}), required=False)
    country = CountryField(blank_label='Select Country')
    postcode = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Postcode'}), required=False)
    facebook = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'https://www.facebook.com'}), required=False)
    twitter = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'https://www.twitter.com'}), required=False)
    instagram = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'https://www.instagram.com'}), required=False)
    youtube = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'https://www.youtube.com'}), required=False)
    password = None

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profile_image', 'email_address',
                  'car_model', 'city', 'county', 'country', 'postcode',
                  'facebook', 'twitter', 'instagram', 'youtube']

