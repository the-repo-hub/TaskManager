from django import forms
from django.contrib.auth import get_user_model
from tasks.models import Task
from bootstrap_datepicker_plus.widgets import DatePickerInput
from tasks.choices import TaskChoices

User = get_user_model()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'executor', 'deadline', 'status')

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))
    executor = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-select mb-3'}),
        queryset=User.objects.get_queryset(),
        required=False,
    )
    deadline = forms.DateField(widget=DatePickerInput(), required=False)
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-select mb-3'}),
        choices=TaskChoices,
    )
