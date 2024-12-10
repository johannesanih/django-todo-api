from django.db import models

# Create your models here.
class Todo(models.Model):
	owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)
	title = models.CharField(max_length=80, blank=False)
	description = models.CharField(max_length=200, blank=True)
	done = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']