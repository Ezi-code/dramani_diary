from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import BlogPost


class PostListView(ListView):
    """post list view."""

    model = BlogPost
    template_name = "blog/list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    """post detail view."""

    model = BlogPost
    template_name = "blog/post_detail.html"


class PostCreateView(CreateView):
    """"""

    model = BlogPost
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostUpdateView(UpdateView):
    """"""

    model = BlogPost
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostDeleteView(DeleteView):
    """"""

    model = BlogPost
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
