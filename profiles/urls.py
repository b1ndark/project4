from django.urls import path, include
from . import views
from .views import UserProfiles


urlpatterns = [
    path("<int:user>/", UserProfiles.as_view(), name="profile"),
    path("signup/", views.signup, name="signup"),
    path("edit_profile/", views.editProfile, name="edit_profile"),
]
