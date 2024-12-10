from rest_framework import serializers
from django.contrib.auth.models import User
from todos.models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	done = serializers.ReadOnlyField()

	class Meta:
		model = Todo
		fields = ['url', 'id', 'title', 'description', 'done', 'owner', 'created']


class UserSerializer(serializers.HyperlinkedModelSerializer):
	username = serializers.ReadOnlyField()
	todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)

	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'todos']