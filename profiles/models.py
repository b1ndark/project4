from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from typerforum.models import CAR_MODELS
from django_countries.fields import CountryField
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    User profile so user can update its details
    example 'city'
    """
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    car_model = models.CharField(
        max_length=30, choices=CAR_MODELS, default="ek9"
    )
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=40, null=True, blank=True)
    country = CountryField(blank_label='Select country', null=True, blank=True)
    postcode = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """
    create an user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
