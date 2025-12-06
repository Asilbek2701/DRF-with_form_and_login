from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView

from .models import Post
from .serializers import PostSerializer


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer