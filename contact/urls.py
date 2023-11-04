from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserContact.as_view(), name='contact'),
]
