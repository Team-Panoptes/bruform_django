from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    published_posts = Post.objects.filter(published_date__lte=timezone.now())

    return render(request, "blog/post_list.html", {"posts": published_posts, "prénom": "Bastien"})


def post_detail(request, post_number):
    post = get_object_or_404(Post, id=post_number)

    return render(request, "blog/post_detail.html", {"post": post})

def post_new(request: HttpRequest):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.publish()
            return redirect("post_detail", post_number=blog_post.id)
    else:  # elif request.method == "GET"
        form = PostForm()

    return render(request, "blog/post_new.html", {"form": form})

def post_edit(request, post_number):
    blog_post = get_object_or_404(Post, id=post_number)

    if request.method == "POST":
        form = PostForm(request.POST, instance=blog_post)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.publish()
            return redirect("post_detail", post_number=blog_post.id)
    else:
        form = PostForm(instance=blog_post)

    return render(request, "blog/post_new.html", {"form": form})