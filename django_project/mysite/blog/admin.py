from django.contrib import admin
from .models.post import Post
from .models.comment import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["body", "name", "active", "created_date"]
    list_filter = ["active", "created_date"]
    search_fields = ["body", "name", "email"]
    actions = ["mark_as_approved"]

    def mark_as_approved(self, request, queryset):
        queryset.update(active=True)


class PostAdmin(admin.ModelAdmin):
    exclude = ["created_date"]
    list_display = ["title", "author"]

admin.site.register(Post, PostAdmin)
