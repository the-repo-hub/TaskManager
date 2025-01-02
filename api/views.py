from rest_framework.viewsets import ModelViewSet

from api.serializers import TaskSerializer
from tasks.models import Task


class TaskViewSet(ModelViewSet):

    queryset = Task.objects.get_queryset()
    serializer_class = TaskSerializer

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)