from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.
class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
