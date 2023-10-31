from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("books", views.BookViewSet, "book")


urlpatterns = [
    path("authors/", views.AuthorView.as_view(), name="author-list"),
    path("authors/<int:pk>", views.AuthorInstanceView.as_view()),
    path("", include(router.urls)),
]
