from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["body", "active"]
    list_filter = ["active"]
    search_fields = ["body"]
    actions = ["mark_as_approved"]

    def mark_as_approved(self, request, queryset):
        queryset.update(active=True)
            





class PostAdmin(admin.ModelAdmin):
    exclude = ["created_date"]
    list_display = ["title", "author"]

admin.site.register(Post, PostAdmin)
