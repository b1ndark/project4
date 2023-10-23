from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from typerforum.models import CAR_MODELS
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile so user can update its details
    example 'email'
    """
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    car_model = models.CharField(
        max_length=30, choices=CAR_MODELS, default="ek9"
    )
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=40, null=True, blank=True)
    country = CountryField(blank_label='Select country', null=True, blank=True)
    postcode = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()


post_save.connect(create_user_profile, sender=User)
