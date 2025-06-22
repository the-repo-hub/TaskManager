from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DetailView

User = get_user_model()

class UserDetailView(DetailView):
    model = User
    queryset = User.objects.all()
    template_name = 'users/profile.html'