from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.shortcuts import reverse
from django.urls import reverse_lazy

"""
Car model list for User to choose one of the List
"""
CAR_MODELS = (
    ('select', ''),
    ('ek9', 'Honda Civic Type R EK9'),
    ('ep3', 'Honda Civic Type R EP3'),
    ('fn2', 'Honda Civic Type R FN2'),
    ('fd2', 'Honda Civic Type R FD2'),
    ('fk2', 'Honda Civic Type R FK2'),
    ('fk8', 'Honda Civic Type R FK8'),
    ('fl5', 'Honda Civic Type R FL5'),
    ('dc2', 'Honda Integra Type R DC2'),
    ('dc5', 'Honda Integra Type R DC5'),
    ('nsx-r', 'Honda NSX Type R'),
    ('cl1', 'Honda Accord Type R'),
)


'''
Forum Post
'''
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    Post Model/Content
    """
    title = models.CharField(max_length=200, unique=True)
    car_model = models.CharField(
        max_length=30, choices=CAR_MODELS, default="")
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    excerpt = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum_detail', args=[self.pk])

    def number_of_likes(self):
        return self.likes.count()


'''
Post Comments
'''


class Comment(models.Model):
    """
    Comment Model/Content
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField(verbose_name=('Update your comment...'))
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)
    likes = models.ManyToManyField(
        User, related_name='comment_like', blank=True)

    class Meta:
        ordering = ['created_on']

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'Comment {self.body} by {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('forum')
