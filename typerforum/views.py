from django.shortcuts import render
from django.views import generic
from .models import Post, Comment


def home(request):
    return render(request, 'index.html')


def forum(request):
    return render(request, 'forum.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'forum.html'
    paginate_by = 4
