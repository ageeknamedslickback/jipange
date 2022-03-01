"""TodoList app serializers."""
from rest_framework import serializers

from todo.models import TodoList, TodoListLine


class TodoListSerializer(serializers.ModelSerializer):
    """TodoList model serializer."""

    class Meta:
        """Define class Meta options."""

        model = TodoList
        fields = "__all__"


class TodoListLineSerializer(serializers.ModelSerializer):
    """TodoList line serializer."""

    class Meta:
        """Define class Meta options."""

        model = TodoListLine
        fields = "__all__"
