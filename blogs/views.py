from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

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
    """"""

    model = Blog
    template_name = "blog/form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostUpdateView(UpdateView):
    """"""

    model = Blog
    template_name = "blog/form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostDeleteView(DeleteView):
    """"""

    model = Blog
    template_name = "blog/confirm_delete.html"
    success_url = reverse_lazy("post_list")
