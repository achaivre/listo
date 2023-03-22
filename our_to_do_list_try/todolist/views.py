from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .models import Task, List
from .forms import TaskForm, ListForm

# Login Imports

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Login Views


class LoginView_ToDo(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


class CreateUserPage(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateUserPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super(CreateUserPage, self).get(*args, **kwargs)


# List Views
class AllLists(LoginRequiredMixin, ListView):
    model = List
    context_object_name = "lists"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lists"] = context["lists"].filter(user=self.request.user)
        return context


class ListUpdate(LoginRequiredMixin, UpdateView):
    model = List
    template_name = "list_form.html"
    fields = ["name", "category"]
    success_url = reverse_lazy("home")


class ListDelete(LoginRequiredMixin, DeleteView):
    model = List
    template_name = "list_form.html"
    context_object_name = "list"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class ListCreate(LoginRequiredMixin, CreateView):
    model = List
    form_class = ListForm
    template_name = "list_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListCreate, self).form_valid(form)


# Task Categories Views


class AllTasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "all_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(
            user=self.request.user, task_list=List.objects.get(id=self.kwargs["pk"])
        )
        context["count"] = context["tasks"].filter(is_complete=False).count()
        return context


class HighPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "high_tasks"
    template_name = "high_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["high_tasks"] = context["high_tasks"].filter(
            user=self.request.user,
            priority="high",
            task_list=List.objects.get(id=self.kwargs["pk"]),
        )
        context["count"] = context["high_tasks"].filter(is_complete=False).count()
        return context


class MediumPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "med_tasks"
    template_name = "med_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["med_tasks"] = context["med_tasks"].filter(
            user=self.request.user,
            priority="medium",
            task_list=List.objects.get(id=self.kwargs["pk"]),
        )
        context["count"] = context["med_tasks"].filter(is_complete=False).count()
        return context


class LowPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "low_tasks"
    template_name = "low_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["low_tasks"] = context["low_tasks"].filter(
            user=self.request.user,
            priority="low",
            task_list=List.objects.get(id=self.kwargs["pk"]),
        )
        context["count"] = context["low_tasks"].filter(is_complete=False).count()
        return context


class Completed_View(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "finished_tasks"
    template_name = "completed_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finished_tasks"] = context["finished_tasks"].filter(
            user=self.request.user,
            is_complete=True,
            task_list=List.objects.get(id=self.kwargs["pk"]),
        )
        context["count"] = context["finished_tasks"].filter(is_complete=True).count()
        return context


# Task Edit/Create/Delete Pages
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_form.html"
    fields = ["title", "priority", "is_complete"]
    success_url = reverse_lazy("all_tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_form.html"
    context_object_name = "task"
    success_url = reverse_lazy("all_tasks")

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("all_tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
