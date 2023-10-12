from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    published_posts = Post.objects.filter(published_date__lte=timezone.now())

    return render(request, "blog/post_list.html", {"posts": published_posts, "prénom": "Bastien"})


def post_detail(request, post_number):
    post = Post.objects.get(id=post_number)

    return render(request, "blog/post_detail.html", {"post": post})
