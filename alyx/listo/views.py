from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, ListForm, TaskForm, Sp_TaskForm
from .models import *
from .decorators import unauthenticated_user

# Create your views here.

# Login Views
@unauthenticated_user
def register_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
        else:
            context = {"form": form}
            return render(request, "register.html", context)
    form = CreateUserForm()
    context = {"form": form}
    return render(request, "register.html", context)


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# List Views:
@login_required(login_url="login")
def home_view(request):
    user = request.user
    lists = List.objects.filter(user=user)
    if len(lists) == 0:
        lists = None
    context = {"lists": lists}
    return render(request, "home.html", context)


@login_required(login_url="login")
def create_list_view(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect("home")
    form = ListForm()
    context = {"form": form}
    return render(request, "list_form.html", context)


@login_required(login_url="login")
def delete_list_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    if request.method == "POST":
        list_obj.delete()
        return redirect("home")
    context = {"list": list_obj}
    return render(request, "list_delete.html", context)


@login_required(login_url="login")
def update_list_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    if request.method == "POST":
        form = ListForm(request.POST, instance=list_obj)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = ListForm(instance=list_obj)
    context = {"form": form}
    return render(request, "list_form.html", context)


@login_required(login_url="login")
def list_detail_all_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(user=request.user, task_list=list_obj)
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(user=request.user, task_list=list_obj, is_complete=False)
    )
    count_total = len(Task.objects.filter(user=request.user, task_list=list_obj))
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    return render(request, "all_tasks.html", context)


@login_required(login_url="login")
def list_detail_low_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(user=request.user, task_list=list_obj, priority="low")
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(
            user=request.user, task_list=list_obj, is_complete=False, priority="low"
        )
    )
    count_total = len(
        Task.objects.filter(user=request.user, task_list=list_obj, priority="low")
    )
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    return render(request, "low_tasks.html", context)


@login_required(login_url="login")
def list_detail_med_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(
        user=request.user, task_list=list_obj, priority="medium"
    )
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(
            user=request.user, task_list=list_obj, is_complete=False, priority="medium"
        )
    )
    context = {"list_obj": list_obj, "tasks": tasks, "count": count}
    return render(request, "med_tasks.html", context)


@login_required(login_url="login")
def list_detail_high_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(user=request.user, task_list=list_obj, priority="high")
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(
            user=request.user, task_list=list_obj, is_complete=False, priority="high"
        )
    )
    count_total = len(
        Task.objects.filter(user=request.user, task_list=list_obj, priority="high")
    )
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    return render(request, "high_tasks.html", context)


@login_required(login_url="login")
def list_detail_complete_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(user=request.user, task_list=list_obj, is_complete=True)
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(user=request.user, task_list=list_obj, is_complete=True)
    )
    count_total = len(Task.objects.filter(user=request.user, task_list=list_obj))
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    return render(request, "completed_tasks.html", context)


# Task Views


@login_required(login_url="login")
def create_task_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.task_list = list_obj
            obj.save()
            return redirect(f"/all_tasks_list/{list_obj.id}")
    form = TaskForm()
    context = {"form": form}
    return render(request, "task_form.html", context)


@login_required(login_url="login")
def delete_task_view(request, list_id, task_id):
    list_obj = List.objects.get(id=list_id)
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect(f"/all_tasks_list/{list_obj.id}")
    context = {"task": task, "list_obj": list_obj}
    return render(request, "task-delete.html", context)


@login_required(login_url="login")
def update_task_view(request, list_id, task_id):
    list_obj = List.objects.get(id=list_id)
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f"/all_tasks_list/{list_obj.id}")
    form = TaskForm(instance=task)
    context = {"form": form}
    return render(request, "task_form.html", context)


# ======== SPANISH VIEWS =============
@unauthenticated_user
def sp_register_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("sp_login")
        else:
            context = {"form": form}
            return render(request, "spanish/sp_register.html", context)
    form = CreateUserForm()
    context = {"form": form}
    return render(request, "spanish/sp_register.html", context)


@unauthenticated_user
def sp_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("sp_home")
    return render(request, "registration/sp_login.html")


def sp_logout_view(request):
    logout(request)
    return render(request, "registration/sp_logged_out.html")


# List Views:
@login_required(login_url="login")
def sp_home_view(request):
    user = request.user
    lists = List.objects.filter(user=user)
    if len(lists) == 0:
        lists = None
    context = {"lists": lists}
    return render(request, "spanish/sp_home.html", context)


@login_required(login_url="login")
def sp_create_list_view(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect("sp_home")
    form = ListForm()
    context = {"form": form}
    return render(request, "spanish/sp_list_form.html", context)


@login_required(login_url="login")
def sp_delete_list_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    if request.method == "POST":
        list_obj.delete()
        return redirect("sp_home")
    context = {"list": list_obj}
    return render(request, "spanish/sp_list_delete.html", context)


@login_required(login_url="login")
def sp_update_list_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    if request.method == "POST":
        form = ListForm(request.POST, instance=list_obj)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = ListForm(instance=list_obj)
    context = {"form": form}
    return render(request, "spanish/sp_list_form.html", context)


@login_required(login_url="login")
def sp_list_detail_all_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(user=request.user, task_list=list_obj)
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(user=request.user, task_list=list_obj, is_complete=False)
    )
    count_total = len(Task.objects.filter(user=request.user, task_list=list_obj))
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    return render(request, "spanish/sp_all_tasks.html", context)


@login_required(login_url="login")
def sp_list_detail_low_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(user=request.user, task_list=list_obj, priority="low")
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(
            user=request.user, task_list=list_obj, is_complete=False, priority="low"
        )
    )
    count_total = len(
        Task.objects.filter(user=request.user, task_list=list_obj, priority="low")
    )
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    return render(request, "spanish/sp_low_tasks.html", context)


@login_required(login_url="login")
def sp_list_detail_med_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(
        user=request.user, task_list=list_obj, priority="medium"
    )
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(
            user=request.user, task_list=list_obj, is_complete=False, priority="medium"
        )
    )
    count_total = len(
        Task.objects.filter(user=request.user, task_list=list_obj, priority="medium")
    )
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    context = {"list_obj": list_obj, "tasks": tasks, "count": count}
    return render(request, "spanish/sp_med_tasks.html", context)


@login_required(login_url="login")
def sp_list_detail_high_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(user=request.user, task_list=list_obj, priority="high")
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(
            user=request.user, task_list=list_obj, is_complete=False, priority="high"
        )
    )
    count_total = len(
        Task.objects.filter(user=request.user, task_list=list_obj, priority="high")
    )
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    context = {"list_obj": list_obj, "tasks": tasks, "count": count}
    return render(request, "spanish/sp_high_tasks.html", context)


@login_required(login_url="login")
def sp_list_detail_complete_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    tasks = Task.objects.filter(user=request.user, task_list=list_obj, is_complete=True)
    if len(tasks) == 0:
        tasks = None
    count = len(
        Task.objects.filter(user=request.user, task_list=list_obj, is_complete=True)
    )
    count_total = len(Task.objects.filter(user=request.user, task_list=list_obj))
    context = {
        "list_obj": list_obj,
        "tasks": tasks,
        "count": count,
        "total": count_total,
    }
    return render(request, "spanish/sp_completed_tasks.html", context)


# Task Views


@login_required(login_url="login")
def sp_create_task_view(request, list_id):
    list_obj = List.objects.get(id=list_id)
    if request.method == "POST":
        form = Sp_TaskForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.task_list = list_obj
            obj.save()
            return redirect(f"/sp_all_tasks_list/{list_obj.id}")
    form = Sp_TaskForm()
    context = {"form": form}
    return render(request, "spanish/sp_task_form.html", context)


@login_required(login_url="login")
def sp_delete_task_view(request, list_id, task_id):
    list_obj = List.objects.get(id=list_id)
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect(f"/sp_all_tasks_list/{list_obj.id}")
    context = {"task": task, "list_obj": list_obj}
    return render(request, "spanish/sp_task-delete.html", context)


@login_required(login_url="login")
def sp_update_task_view(request, list_id, task_id):
    list_obj = List.objects.get(id=list_id)
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = Sp_TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f"/sp_all_tasks_list/{list_obj.id}")
    form = Sp_TaskForm(instance=task)
    context = {"form": form}
    return render(request, "spanish/sp_task_form.html", context)
