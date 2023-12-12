from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.PostList.as_view(), name="forum"),
    path('forum/<int:pk>/',
         views.PostDetail.as_view(), name='forum_detail'),
    path('forum/like/<int:pk>', views.PostLike.as_view(), name='post_like'),
    path('forum/post/add_post/', views.AddPost.as_view(), name='add_post'),
    path('forum/edit/<int:pk>/',
         views.EditPost.as_view(), name='edit_post'),
    path('forum/edit/<int:pk>/delete/',
         views.DeletePost.as_view(), name='delete_post'),
    path('forum/edit/comment/<int:pk>/',
         views.EditComment.as_view(), name='edit_comment'),
    path('forum/edit/<int:pk>/delete_comment/',
         views.DeleteComment.as_view(), name='delete_comment'),
]
