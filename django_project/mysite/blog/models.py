from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def get_absolute_url(self):
        # Simpler version (but hardcoded):
        # return f"/post/{self.id}/"
        return reverse("post_detail", kwargs={"post_number": self.id})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"post_number": self.post.id})

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.body
