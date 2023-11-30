from django.urls import path, include
from . import views
from .views import UserProfiles


urlpatterns = [
    path('<int:pk>/', UserProfiles.as_view(), name='profile'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/edit_profile/',
         views.EditProfile.as_view(), name='edit_profile'),
]
