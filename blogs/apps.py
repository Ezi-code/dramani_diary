from django.apps import AppConfig


class BlogsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blogs"

    def ready(self):
        """Import signals."""
        import blogs.signals  # noqa F401
