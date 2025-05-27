"""blog views module."""

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q

from .filters import BlogFilter
from .models import Blog


class PostListView(ListView):
    """post list view."""

    model = Blog
    template_name = "blog/list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    """post detail view."""

    model = Blog
    context_object_name = "post"
    template_name = "blog/details.html"


class PostCreateView(CreateView):
    """post create view."""

    model = Blog
    template_name = "blog/form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostUpdateView(UpdateView):
    """post update view."""

    model = Blog
    template_name = "blog/form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostDeleteView(DeleteView):
    """post delete view."""

    model = Blog
    template_name = "blog/confirm_delete.html"
    success_url = reverse_lazy("post_list")


class SearchView(ListView):
    """Search view for blog posts."""

    model = Blog
    template_name = "blog/search.html"
    context_object_name = "posts"
    filterset_class = BlogFilter
    paginate_by = 10