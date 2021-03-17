from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template = 'blog/blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template = 'blog/post_detail.html'
