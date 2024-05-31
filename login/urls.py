from django.urls import path
from login.views import UserLogin

urlpatterns = [
    path('', UserLogin.as_view(), name='login'),
]
