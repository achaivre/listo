from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["title"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "priority", "is_complete"]
