from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    """
    Render Home Page
    """
    return render(request, 'index.html')


class PostList(generic.ListView):
    """
    Render Forum Page and display the Posts
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'forum.html'
    paginate_by = 4

    def get_queryset(self, **kwargs):
        """
        Searh for a post
        """
        query = self.request.GET.get('q')

        if query:

            posts = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(car_model__icontains=query)
            )
        else:
            if query == '':
                messages.add_message(
                    self.request, messages.ERROR, "No results found. Please try Post 'title'")
            posts = Post.objects.all()

        return posts


class PostDetail(View):
    """
    Render Forum Detail Page and display the Post and its Comments
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'forum_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(self.request, messages.SUCCESS,
                                 "Your comment has been added to the Post")
            return HttpResponseRedirect('../')
        else:
            comment_form = CommentForm()

        return render(
            request,
            'forum_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm(),
                'liked': liked
            },
        )


class AddPost(SuccessMessageMixin, generic.CreateView):
    """
    Render Forum Add Post Page so User can a Add Post
    """
    model = Post
    template_name = 'forum_add_post.html'
    fields = ('title', 'slug', 'author', 'car_model',
              'featured_image', 'content', 'excerpt',)
    success_message = "Your Post has been added"


class EditPost(SuccessMessageMixin, generic.UpdateView):
    """
    Render Forum Edit Post Page so User can a Edit Post
    """
    model = Post
    template_name = 'forum_edit_post.html'
    fields = ('title', 'car_model', 'featured_image', 'content',)
    success_message = "Your Post has been Updated"


class DeletePost(SuccessMessageMixin, generic.DeleteView):
    """
    Render Forum Delete Post Page so User can a Delete Post
    and redirect to forum
    """
    model = Post
    template_name = 'forum_delete_post.html'

    success_url = reverse_lazy('forum_detail')
    success_message = "Your Post has been Deleted"


class EditComment(SuccessMessageMixin, generic.UpdateView):
    """
    Render Forum Edit Comment Page so User can a Edit Post
    """
    model = Comment
    template_name = 'forum_edit_comment.html'
    fields = ('body',)
    success_message = "Your Comment has been Updated"


class DeleteComment(SuccessMessageMixin, generic.DeleteView):
    """
    Render Forum Delete Comment Page so User can a Delete Comment
    and redirect to forum
    """
    model = Comment
    template_name = 'forum_delete_comment.html'

    success_url = reverse_lazy('forum')
    success_message = "Your Comment has been Deleted"


class PostLike(View):
    """
    To like Posts
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.add_message(self.request, messages.ERROR,
                                 "You have unliked the Post")
        else:
            post.likes.add(request.user)
            messages.add_message(self.request, messages.SUCCESS,
                                 "You have liked the Post")

        return HttpResponseRedirect(reverse('forum_detail', args=[slug]))


class CommentLike(View):
    """
    To like Posts
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.add_message(self.request, messages.ERROR,
                                 "You have unliked the Post")
        else:
            post.likes.add(request.user)
            messages.add_message(self.request, messages.SUCCESS,
                                 "You have liked the Post")

        return HttpResponseRedirect(reverse('forum_detail', args=[slug]))
