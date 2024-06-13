from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from tasks.forms import TaskForm
from tasks.models import Task


class TaskBaseMixin(LoginRequiredMixin):

    queryset = Task.objects.get_queryset()
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')

# TODO: remove ListView mixin


class TaskBoard(TaskBaseMixin, ListView):

    template_name = 'tasks/board.html'


class TaskList(TaskBaseMixin, ListView):

    template_name = 'tasks/list.html'


class TaskCreate(TaskBaseMixin, CreateView):

    template_name = 'tasks/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class TaskUpdate(TaskBaseMixin, UpdateView):

    template_name = 'tasks/create.html'


class TaskDetail(TaskBaseMixin, DetailView):

    template_name = 'tasks/detail.html'
