from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from tasks.forms import TaskForm
from tasks.models import Task


class TaskBaseMixin(LoginRequiredMixin):

    queryset = Task.objects.get_queryset()
    model = Task
    context_object_name = 'object'
    form_class = TaskForm


class TaskBoard(TaskBaseMixin, ListView):

    template_name = 'tasks/board.html'


class TaskList(TaskBaseMixin, ListView):

    template_name = 'tasks/list.html'


class TaskCreate(TaskBaseMixin, CreateView):

    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:board')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
