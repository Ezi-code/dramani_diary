"""blog admin file."""

from django.contrib import admin
from blogs.models import Blog


class BlogPageAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date"]
    search_fields = ["title", "author"]
    list_filter = ["published_date", "author", "featured_by"]


admin.site.register(Blog, BlogPageAdmin)
# admin.site.register(BlogPe, BlogPageAdmin)
