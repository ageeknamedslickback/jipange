"""Todo app views."""
from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import TodoList, TodoListLine
from todo.serializers import TodoListLineSerializer, TodoListSerializer


class TodoListView(APIView):
    """TodoList API views."""

    def get(self, request):
        """Handle any GET request to this view."""
        todo_lists = TodoList.objects.all()
        serialized_data = TodoListSerializer(todo_lists, many=True)
        return Response(
            data={"todo_lists": serialized_data.data}, status=HTTPStatus.OK
        )

    def post(self, request):
        """Handle any POST request to this view."""
        data = {
            "list_name": request.data.get("list_name"),
            "description": request.data.get("description"),
        }
        serialized_data = TodoListSerializer(data=data)
        if not serialized_data.is_valid():
            return Response(
                serialized_data.errors, status=HTTPStatus.BAD_REQUEST
            )
        serialized_data.save()
        return Response(
            data={"todo_list": serialized_data.data}, status=HTTPStatus.CREATED
        )


class TodoListLineView(APIView):
    """TodoList line API View."""

    def get(self, request, pk):
        """Handle any GET request to this view."""
        todo_list_lines = TodoListLine.objects.filter(todo_list__id=pk)
        serialized_data = TodoListLineSerializer(todo_list_lines, many=True)
        return Response(
            data={"todo_lists_lines": serialized_data.data},
            status=HTTPStatus.OK,
        )

    def post(self, request, pk):
        """Handle any POST request to this view."""
        description = None
        scheduled_at = None
        if request.data.get("description"):
            description = request.data.get("description")

        if request.data.get("scheduled_at"):
            scheduled_at = request.data.get("scheduled_at")

        data = {
            "todo_list": pk,
            "title": request.data.get("title"),
            "description": description,
            "scheduled_at": scheduled_at,
        }

        serialized_data = TodoListLineSerializer(data=data)
        if not serialized_data.is_valid():
            return Response(
                serialized_data.errors, status=HTTPStatus.BAD_REQUEST
            )
        serialized_data.save()
        return Response(
            data={"todo_list_line": serialized_data.data},
            status=HTTPStatus.CREATED,
        )
