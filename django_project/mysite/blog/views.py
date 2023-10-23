from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, ModelFormMixin
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, CommentForm


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


class PostDetail(ModelFormMixin, DetailView):
    model = Post
    form_class = CommentForm

    # slug_field = "id"
    # slug_url_kwarg = "post_number"
    pk_url_kwarg = "post_number"
    context_object_name = "post"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(active=True)
        return context

    def post(self, request, post_number):

        form = self.get_form()

        self.object = self.get_object()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.post = self.object
        new_comment.save()
        
        return super().form_valid(form)



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
    

class PostPublish(RedirectView):
    
    pattern_name = "post_detail"

    def get_redirect_url(self, *args, **kwargs):
        blog_post = get_object_or_404(Post, id=kwargs["post_number"])
        blog_post.publish()
        return super().get_redirect_url(*args, **kwargs)


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
