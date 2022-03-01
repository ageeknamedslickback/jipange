"""TodoList models."""
import uuid

from django.db import models


class AbstractBaseModel(models.Model):
    """
    An abstract base class model.

    It provides shared fields that are self-updating.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        """Define class Meta options."""

        abstract = True


class TodoList(AbstractBaseModel):
    """
    Defines a Todo List.

    This is a named list that contains Todo items
    """

    list_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # Here for the purpose of getting to know signals
    items_count = models.IntegerField(null=True, blank=True)


class TodoListLine(AbstractBaseModel):
    """Defines the items/reminders in a Todo List."""

    todo_list = models.ForeignKey("TodoList", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    sub_line = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
