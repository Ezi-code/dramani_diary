from django.contrib import admin
from blogs.models import BlogPost


class BlogPageAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date"]
    search_fields = ["title", "author"]
    list_filter = ["published_date", "author", "featured_by"]


admin.site.register(BlogPost, BlogPageAdmin)
# admin.site.register(BlogPe, BlogPageAdmin)
