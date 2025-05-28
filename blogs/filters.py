"""blog filters."""

from django_filters import filterset
from .models import Blog


class BlogFilter(filterset.FilterSet):
    """Filter for blog posts."""

    class Meta:
        model = Blog
        fields = {
            "title": ["icontains"],
            "content": ["icontains"],
            "category": ["exact"],
            "tags": ["exact", "icontains"],
            "created_at": ["exact", "year__gt", "year__lt"],
        }
