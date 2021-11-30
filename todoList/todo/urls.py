"""TodoList app URL conf."""
from django.urls import path

from todo.views import TodoListLineView, TodoListView

urlpatterns = [
    path("lists/", TodoListView.as_view(), name="lists"),
    path(
        "list/<str:pk>/lines/",
        TodoListLineView.as_view(),
        name="list_lines",
    ),
]
