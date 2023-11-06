from django.db import models
from django.shortcuts import reverse
from typerforum.models import CAR_MODELS


class UserContact(models.Model):
    """
    User Contact Model
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    car_model = models.CharField(
        max_length=30, choices=CAR_MODELS, default="")
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
