from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:post_number>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:post_number>/edit/", views.post_edit, name='post_edit'),
    path("drafts/", views.post_draft_list, name="post_draft_list"),
    path("post/<int:post_number>/publish/", views.post_publish, name="post_publish"),
    path("post/<int:post_number>/delete/", views.post_delete, name="post_delete"),
]
