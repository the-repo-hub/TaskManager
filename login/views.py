from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# TODO make easier


class UserLogin(LoginView):

    template_name = 'login/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return redirect('tasks:board')


class UserLogout(LogoutView):

    template_name = 'login/login.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
