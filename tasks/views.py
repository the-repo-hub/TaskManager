from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View, CreateView

from tasks.models import Task


class TaskBaseMixin(LoginRequiredMixin):

    queryset = Task.objects.get_queryset()
    model = Task
    context_object_name = 'object'


class TaskBoard(TaskBaseMixin, ListView):

    template_name = 'tasks/board.html'


class TaskList(TaskBaseMixin, ListView):

    template_name = 'tasks/list.html'


class TaskCreate(TaskBaseMixin, CreateView):

    template_name = 'tasks/create.html'
    fields = '__all__'
