from django.db import models
from django.contrib.auth import get_user_model
from tasks.choices import TaskChoices

User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, blank=True, default=None, null=True, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=255, default=TaskChoices.available.value, choices=TaskChoices)

    def __str__(self):
        return self.title


