"""TodoList models tests."""
from datetime import datetime

import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient

from todo.models import TodoList, TodoListLine

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

    def test_create_todo_list_line(self):
        """Test creation of a list's items."""
        todo_list = baker.make(
            TodoList,
            list_name="Test List",
            description="List that we are going to use for tests",
        )
        todo_list_line = baker.make(
            TodoListLine,
            todo_list=todo_list,
            title="First Item to be done",
            description="First list item that should be done",
        )

        assert TodoListLine.objects.count() == 1
        assert todo_list_line.todo_list.id == todo_list.id


class TestViews:
    """Tests for views."""

    def test_post_todo_list(self):
        """Test POST requests to add a todo list."""
        client = APIClient()
        response = client.post("/not-a-path")
        assert response.status_code == 404

        payload = {"not-list_name": "Not a list name"}
        response = client.post("/api/v1/lists/", payload)
        assert response.status_code == 400

        payload = {
            "list_name": "Test list",
            "description": "Test list description",
        }
        response = client.post("/api/v1/lists/", payload)
        assert response.status_code == 201
        assert TodoList.objects.count() == 1

    def test_get_todo_list(self):
        """Test GET requests to get a todo list."""
        client = APIClient()
        payload = {
            "list_name": "Test list",
            "description": "Test list description",
        }
        response = client.post("/api/v1/lists/", payload)
        assert response.status_code == 201
        assert TodoList.objects.count() == 1

        response = client.get("/api/v1/lists/")
        resp_data = response.json()
        assert response.status_code == 200
        assert "todo_lists" in resp_data
        assert len(resp_data["todo_lists"]) == 1

    def test_post_todo_list_lines(self):
        """Test POST requests to add a todo list items."""
        client = APIClient()
        payload = {
            "list_name": "Test list",
            "description": "Test list description",
        }
        resp = client.post("/api/v1/lists/", payload)
        assert resp.status_code == 201
        assert TodoList.objects.count() == 1

        id = resp.json()["todo_list"]["id"]
        line_payload = {
            "todo_list": id,
            "title": "Todo list line(item)",
            "description": "Todo list line(item) description",
            "scheduled_at": str(datetime.now()),
        }
        url = reverse("list_lines", args=[id])
        response = client.post(url, line_payload)
        assert response.status_code == 201
        assert TodoListLine.objects.count() == 1

        line_payload = {
            "todo_list": id,
        }
        url = reverse("list_lines", args=[id])
        response = client.post(url, line_payload)
        assert response.status_code == 400

    def test_get_todo_list_lines(self):
        """Test GET requests to get a todo list items."""
        client = APIClient()
        payload = {
            "list_name": "Test list",
            "description": "Test list description",
        }
        resp = client.post("/api/v1/lists/", payload)
        assert resp.status_code == 201
        assert TodoList.objects.count() == 1

        id = resp.json()["todo_list"]["id"]
        line_payload = {
            "todo_list": id,
            "title": "Todo list line(item)",
            "description": "Todo list line(item) description",
        }
        url = reverse("list_lines", args=[id])
        response = client.post(url, line_payload)
        assert response.status_code == 201

        response = client.get(url)
        resp_data = response.json()
        assert response.status_code == 200
        assert "todo_lists_lines" in resp_data
        assert len(resp_data["todo_lists_lines"]) == 1
