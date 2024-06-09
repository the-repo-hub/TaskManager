from django.urls import path
from tasks.views import TaskBoard, TaskList, TaskCreate

urlpatterns = [
    path('', TaskBoard.as_view(), name='board'),
    path('list/', TaskList.as_view(), name='list'),
    path('create/', TaskCreate.as_view(), name='create'),
]
