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
    is_complete = forms.BooleanField(label="Complete", required=False)

    class Meta:
        model = Task
        fields = ["title", "priority", "is_complete"]


class Sp_TaskForm(forms.ModelForm):
    PRIORITY_CHOICES = (("high", "ALTO"), ("medium", "MEDIA"), ("low", "BAJA"))
    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES, required=True, label="Prioridad"
    )
    title = forms.CharField(max_length=50, required=True, label="Nombre")
    is_complete = forms.BooleanField(label="Completo", required=False)

    class Meta:
        model = Task
        fields = ["title", "priority", "is_complete"]
