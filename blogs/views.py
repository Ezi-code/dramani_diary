from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import BlogPage


class PostListView(ListView):
    """post list view."""

    model = BlogPage
    template_name = "blog/home.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    """post detail view."""

    model = BlogPage
    template_name = "blog/post_detail.html"


class PostCreateView(CreateView):
    """"""

    model = BlogPage
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostUpdateView(UpdateView):
    """"""

    model = BlogPage
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostDeleteView(DeleteView):
    """"""

    model = BlogPage
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
