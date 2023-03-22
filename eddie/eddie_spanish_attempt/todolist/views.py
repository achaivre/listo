from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .models import Task
from .forms import TaskForm

# Login Imports

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Login Views


class LoginView_ToDo(LoginView):
    template_name = "english/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("all_tasks")


class CreateUserPage(FormView):
    template_name = "english/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("all_tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateUserPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("all_tasks")
        return super(CreateUserPage, self).get(*args, **kwargs)


# Task Categories Views


class AllTasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "english/all_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(is_complete=False).count()
        return context


class HighPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "high_tasks"
    template_name = "english/high_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["high_tasks"] = context["high_tasks"].filter(
            user=self.request.user, priority="high"
        )
        context["count"] = context["high_tasks"].filter(is_complete=False).count()
        return context


class MediumPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "med_tasks"
    template_name = "english/med_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["med_tasks"] = context["med_tasks"].filter(
            user=self.request.user, priority="medium"
        )
        context["count"] = context["med_tasks"].filter(is_complete=False).count()
        return context


class LowPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "low_tasks"
    template_name = "english/low_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["low_tasks"] = context["low_tasks"].filter(
            user=self.request.user, priority="low"
        )
        context["count"] = context["low_tasks"].filter(is_complete=False).count()
        return context


class Completed_View(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "finished_tasks"
    template_name = "english/completed_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finished_tasks"] = context["finished_tasks"].filter(
            user=self.request.user, is_complete=True
        )
        context["count"] = context["finished_tasks"].filter(is_complete=True).count()
        return context


# Task Edit/Create/Delete Pages
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "english/task_form.html"
    fields = ["title", "priority", "is_complete"]
    success_url = reverse_lazy("all_tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "english/task_form.html"
    context_object_name = "task"
    success_url = reverse_lazy("all_tasks")

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "english/task_form.html"
    success_url = reverse_lazy("all_tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


# Spanish Views


class Sp_LoginView_ToDo(LoginView):
    template_name = "spanish/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("all_tasks")


class Sp_CreateUserPage(FormView):
    template_name = "spanish/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("all_tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateUserPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("all_tasks")
        return super(CreateUserPage, self).get(*args, **kwargs)


# Task Categories Views


class Sp_AllTasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "spanish/all_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(is_complete=False).count()
        return context


class Sp_HighPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "high_tasks"
    template_name = "spanish/high_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["high_tasks"] = context["high_tasks"].filter(
            user=self.request.user, priority="high"
        )
        context["count"] = context["high_tasks"].filter(is_complete=False).count()
        return context


class Sp_MediumPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "med_tasks"
    template_name = "spanish/med_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["med_tasks"] = context["med_tasks"].filter(
            user=self.request.user, priority="medium"
        )
        context["count"] = context["med_tasks"].filter(is_complete=False).count()
        return context


class Sp_LowPriority(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "low_tasks"
    template_name = "spanish/low_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["low_tasks"] = context["low_tasks"].filter(
            user=self.request.user, priority="low"
        )
        context["count"] = context["low_tasks"].filter(is_complete=False).count()
        return context


class Sp_Completed_View(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "finished_tasks"
    template_name = "spanish/completed_tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finished_tasks"] = context["finished_tasks"].filter(
            user=self.request.user, is_complete=True
        )
        context["count"] = context["finished_tasks"].filter(is_complete=True).count()
        return context


# Task Edit/Create/Delete Pages
class Sp_TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "spanish/task_form.html"
    fields = ["title", "priority", "is_complete"]
    success_url = reverse_lazy("all_tasks")


class Sp_TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "spanish/task_form.html"
    context_object_name = "task"
    success_url = reverse_lazy("all_tasks")

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class Sp_TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "spanish/task_form.html"
    success_url = reverse_lazy("all_tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
