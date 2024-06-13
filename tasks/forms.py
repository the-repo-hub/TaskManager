from django import forms
from django.contrib.auth import get_user_model
from tasks.models import Task
from bootstrap_datepicker_plus.widgets import DatePickerInput

User = get_user_model()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'executor', 'deadline')

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))
    executor = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-select mb-3'}),
        queryset=User.objects.get_queryset(),
    )
    deadline = forms.DateField(widget=DatePickerInput())
