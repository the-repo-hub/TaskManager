from django.urls import path
from tasks.views import TaskBoard

urlpatterns = [
    path('', TaskBoard.as_view(), name='board'),
]
