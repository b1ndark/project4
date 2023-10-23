from django.urls import path
from . import views
from .views import UserProfiles


urlpatterns = [
    path("<slug:user>/", UserProfiles.as_view(), name="profile"),
]
