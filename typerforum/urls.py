from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.PostList.as_view(), name="forum"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='forum_detail'),
]
