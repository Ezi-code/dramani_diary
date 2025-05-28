"""home views."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page view."""

    template_name = "home/home.html"


class AboutView(TemplateView):
    """About page view."""

    template_name = "home/about.html"
