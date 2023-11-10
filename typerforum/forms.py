from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """
    Comment Form
    """
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {
            'body': 'Write a comment...'
        }


class PostForm(forms.ModelForm):
    """
    Post Form
    """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'car_model',
                  'featured_image', 'content', 'excerpt',)
