from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:post_number>/", views.post_detail, name="post_detail"),
]
