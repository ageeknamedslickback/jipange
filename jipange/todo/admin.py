"""Todo app admin."""
from django.contrib import admin

from .models import TodoList, TodoListLine

admin.site.register(TodoList)
admin.site.register(TodoListLine)
