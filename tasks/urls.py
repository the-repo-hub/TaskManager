from django.urls import path
from tasks.views import TaskBoard, TaskList

urlpatterns = [
    path('', TaskBoard.as_view(), name='board'),
    path('list/', TaskList.as_view(), name='task'),
]
