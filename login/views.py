from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect
from django.urls import reverse_lazy



class UserLogin(LoginView):

    template_name = 'login/login.html'
    success_url = reverse_lazy('tasks:board')



class UserLogout(LogoutView):

    template_name = 'login/login.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
