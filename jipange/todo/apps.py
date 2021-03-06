"""TodoList app configuration."""
from django.apps import AppConfig


class TodoConfig(AppConfig):
    """TodoList appconfiguration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "todo"

    def ready(self):
        import todo.signals
