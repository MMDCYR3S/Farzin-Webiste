from django.contrib import admin
from blog.models import Post, Category

# Blog admin panel
class PostAdminPanel(admin.ModelAdmin):
    list_display = (
        "title",
        "photographer",
        "status",
        "counted_views",
        "counted_likes",
        "created_date",
        "published_date",
    )
    list_filter = ("photographer", "status", "published_date")
    search_fields = ("title", "content")
    
admin.site.register(Post, PostAdminPanel)
admin.site.register(Category)
