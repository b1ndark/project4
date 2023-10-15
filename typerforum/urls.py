from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.forum, name='forum'),
]
