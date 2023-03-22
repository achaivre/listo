from django import forms
from .models import Task, List


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "priority", "is_complete"]


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["name", "category"]
