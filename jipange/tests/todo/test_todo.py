"""TodoList models tests."""
import pytest
from model_bakery import baker

from todo.models import TodoList

pytestmark = pytest.mark.django_db


class TestModels:
    """Tests for models."""

    def test_create_todo_list(self):
        """Test the creation of a todo list."""
        todo_list = baker.make(
            TodoList,
            list_name="Test List",
            description="List that we are going to use for tests",
        )
        assert len(TodoList.objects.all()) == 1
        assert todo_list.list_name == "Test List"


class TestSerializers:
    """Tests for serializers."""

    pass


class TestViews:
    """Tests for views."""

    pass


class TestSignals:
    """Tests for signals."""

    pass
