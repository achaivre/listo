"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from listo.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("register", register_view, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("create_list/", create_list_view, name="create_list"),
    path("update_list/<int:list_id>/", update_list_view, name="update_list"),
    path("delete_list/<int:list_id>/", delete_list_view, name="delete_list"),
    path("all_tasks_list/<int:list_id>/", list_detail_all_view, name="all_tasks"),
    path("low_tasks_list/<int:list_id>/", list_detail_low_view, name="low_tasks"),
    path("med_tasks_list/<int:list_id>/", list_detail_med_view, name="med_tasks"),
    path("high_tasks_list/<int:list_id>/", list_detail_high_view, name="high_tasks"),
    path(
        "completed_tasks_list/<int:list_id>/",
        list_detail_complete_view,
        name="completed_tasks",
    ),
    path("task_create/<int:list_id>/", create_task_view, name="create_task"),
    path(
        "task_update/<int:list_id>/<int:task_id>/",
        update_task_view,
        name="update_task",
    ),
    path(
        "task_delete/<int:list_id>/<int:task_id>/",
        delete_task_view,
        name="delete_task",
    ),
    # spanish urls
    path("sp_casa/", sp_home_view, name="sp_home"),
    path("sp_register", sp_register_view, name="sp_register"),
    path("sp_login/", sp_login_view, name="sp_login"),
    path("sp_logout/", sp_logout_view, name="sp_logout"),
    path("sp_create_list/", sp_create_list_view, name="sp_create_list"),
    path("sp_update_list/<int:list_id>/", sp_update_list_view, name="sp_update_list"),
    path("sp_delete_list/<int:list_id>/", sp_delete_list_view, name="sp_delete_list"),
    path(
        "sp_all_tasks_list/<int:list_id>/", sp_list_detail_all_view, name="sp_all_tasks"
    ),
    path(
        "sp_low_tasks_list/<int:list_id>/", sp_list_detail_low_view, name="sp_low_tasks"
    ),
    path(
        "sp_med_tasks_list/<int:list_id>/", sp_list_detail_med_view, name="sp_med_tasks"
    ),
    path(
        "sp_high_tasks_list/<int:list_id>/",
        sp_list_detail_high_view,
        name="sp_high_tasks",
    ),
    path(
        "sp_completed_tasks_list/<int:list_id>/",
        sp_list_detail_complete_view,
        name="sp_completed_tasks",
    ),
    path("sp_task_create/<int:list_id>/", sp_create_task_view, name="sp_create_task"),
    path(
        "sp_task_update/<int:list_id>/<int:task_id>/",
        sp_update_task_view,
        name="sp_update_task",
    ),
    path(
        "sp_task_delete/<int:list_id>/<int:task_id>/",
        sp_delete_task_view,
        name="sp_delete_task",
    ),
]
