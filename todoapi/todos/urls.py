from rest_framework.routers import DefaultRouter
from django.urls import path, include
from todos.views import TodoViewSet, UserViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
	path('', include(router.urls)),
]