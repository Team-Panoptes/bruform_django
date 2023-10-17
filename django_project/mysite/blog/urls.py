from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("post/<int:post_number>/", views.PostDetail.as_view(), name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:post_number>/edit/", views.post_edit, name='post_edit'),
    path("drafts/", views.PostDraftList.as_view(), name="post_draft_list"),
    path("post/<int:post_number>/publish/", views.post_publish, name="post_publish"),
    path("post/<int:post_number>/delete/", views.post_delete, name="post_delete"),
    path("about/", views.About.as_view(), name="about"),
    path("check/<int:post_number>/<str:username>/", views.Check.as_view(), name="check"),
]
