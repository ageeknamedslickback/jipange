"""TodoList app serializers."""
from rest_framework import serializers

from todo.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    """TodoList model serializer."""

    class Meta:
        """Define class Meta options."""

        model = TodoList
        fields = "__all__"
