from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from todos.models import Todo
from todos.serializers import TodoSerializer, UserSerializer
from todos.permissions import IsOwnerOrReadOnly


class TodoViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	@action(detail=True)
	def tickDone(self, request, *args, **kwargs):
		todo = self.get_object()
		st = ""
		if todo.done is True:
			todo.done = False
			st = "undone"
		elif todo.done is False:
			todo.done = True
			st = "done"

		todo.save()

		return Response({
			'status': f'You ticked {todo.title} as {st}',
		}, status = status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer