from django.db import models
from django.urls import reverse
from .post import Post

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
