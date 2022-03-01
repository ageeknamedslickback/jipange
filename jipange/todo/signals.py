"""TodoList app Django signals."""
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TodoList, TodoListLine


@receiver(post_save, sender=TodoListLine)
def notify_item_count_increase(sender, instance, **kwargs):
    """Increament the item count in a list after an item has been added."""
    parent_list = TodoList.objects.get(id=instance.todo_list.id)
    parent_list_lines = TodoListLine.objects.filter(
        todo_list__id=parent_list.id
    )
    parent_list.items_count = len(parent_list_lines)
    parent_list.save()
