from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


# Create your views here.
class PostList(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prenom"] = "Bastien"

        return context


class PostDraftList(ListView):
    queryset = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    template_name = "blog/post_draft_list.html"
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    # slug_field = "id"
    # slug_url_kwarg = "post_number"
    pk_url_kwarg = "post_number"
    context_object_name = "post"

def post_new(request: HttpRequest):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect("post_detail", post_number=blog_post.id)
    else:  # elif request.method == "GET"
        form = PostForm()

    return render(request, "blog/post_new.html", {"form": form})


class PostNew(CreateView):
    model = Post
    fields = ("title", "text")
    template_name = "blog/post_new.html"
    
    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"post_number": self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEdit(UpdateView):
    model = Post
    fields = ("title", "text")
    # Default : "blog/post_update_form.html"
    template_name = "blog/post_new.html"
    pk_url_kwarg = "post_number"
    # success_url = reverse_lazy("post_list")

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"post_number": self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def post_publish(request, post_number):
    blog_post = get_object_or_404(Post, id=post_number)
    blog_post.publish()

    return redirect("post_detail", post_number=blog_post.id)


class PostDelete(DeleteView):
    model = Post
    pk_url_kwarg = "post_number"
    success_url = reverse_lazy("post_list")


class About(TemplateView):
    template_name = "blog/about.html"


class Check(DetailView):
    model = Post
    pk_url_kwarg = "post_number"

    def get(self, request, post_number, username, *args, **kwargs):
        print(post_number)
        print(username)
        return super().get(request, post_number, *args, **kwargs)

def check(requests, post_number, username):
    pass
