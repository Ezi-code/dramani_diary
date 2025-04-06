"""home views."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page view."""

    template_name = "home/home.html"
