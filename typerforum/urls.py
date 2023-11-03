from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.PostList.as_view(), name="forum"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='forum_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('forum/add_post/', views.AddPost.as_view(), name='add_post'),
    path('forum/edit/<slug:slug>/',
         views.EditPost.as_view(), name='edit_post'),
    path('forum/edit/<slug:slug>/delete/',
         views.DeletePost.as_view(), name='delete_post'),
    path('forum/edit/comment/<int:pk>/',
         views.EditComment.as_view(), name='edit_comment'),
]
