from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content', 'car_model']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'likes')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'body', 'post', 'created_on')
    list_filter = ('created_on', 'last_name', 'likes')
    search_fields = ['last_name', 'email address', 'body']
