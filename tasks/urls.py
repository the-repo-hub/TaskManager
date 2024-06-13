from django.urls import path
from tasks.views import TaskBoard, TaskList, TaskCreate, TaskUpdate, TaskDetail

urlpatterns = [
    path('', TaskBoard.as_view(), name='board'),
    path('list/', TaskList.as_view(), name='list'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('<int:pk>', TaskDetail.as_view(), name='detail'),
]
