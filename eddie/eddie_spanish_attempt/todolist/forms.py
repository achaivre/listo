from django import forms
from .models import Task
from django.contrib.auth.forms import User


# class SpanishUserForm(User):
#     # bryan's bull shit
#     class Meta:
#         model = User()
#         fields = ("username", "password")
#         labels = {
#             "username": "Spanish for username",
#             "password": "spanish for password",
#         }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "priority", "is_complete"]

    def __init__(self, *args, **kwargs):
        # bryan's bull shit
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["title"].label = "Titulo"
        self.fields["priority"].label = "Prioridad"
        self.fields["is_complete"].label = "Completo"
