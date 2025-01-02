from rest_framework.viewsets import ModelViewSet

from api.serializers import TaskSerializer
from tasks.models import Task


class TaskViewSet(ModelViewSet):

    queryset = Task.objects.get_queryset()
    serializer_class = TaskSerializer