from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View

from tasks.models import Task


class TaskBaseMixin(LoginRequiredMixin):

    queryset = Task.objects.all()
    model = Task


class TaskBoard(TaskBaseMixin, ListView):

    template_name = 'tasks/board.html'
