"""Todo app views."""
from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import TodoList
from todo.serializers import TodoListSerializer


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
