from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from typerforum.models import CAR_MODELS
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    User profile so user can update its details
    example 'city'
    """
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    email_address = models.EmailField(
        max_length=70, blank=True, default="")
    first_name = models.CharField(
        max_length=100, null=True, blank=True, default="")
    last_name = models.CharField(
        max_length=100, null=True, blank=True, default="")
    car_model = models.CharField(
        max_length=30, choices=CAR_MODELS, default="Select Car model")
    city = models.CharField(max_length=40, null=True, blank=True, default="")
    county = models.CharField(max_length=40, null=True, blank=True, default="")
    country = CountryField(blank_label='Select country',
                           null=True, blank=True, default="")
    postcode = models.CharField(
        max_length=15, null=True, blank=True, default="")
    profile_image = CloudinaryField('image', default='defaultProfilePicture')
    facebook = models.CharField(
        max_length=250, null=True, blank=True, default="")
    twitter = models.CharField(
        max_length=250, null=True, blank=True, default="")
    instagram = models.CharField(
        max_length=250, null=True, blank=True, default="")
    youtube = models.CharField(
        max_length=250, null=True, blank=True, default="")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', args=[self.pk])


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """
    create an user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
