"""TodoList app URL conf."""
from django.urls import path

from todo.views import TodoListView

urlpatterns = [
    path("lists/", TodoListView.as_view(), name="lists"),
]
