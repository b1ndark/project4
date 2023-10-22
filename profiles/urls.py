from django.urls import path
from . import views
from .models import UserProfiles


urlpatterns = [
    path("", UserProfiles.as_view(), name="profile"),
]

