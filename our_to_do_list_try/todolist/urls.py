from django.contrib import admin
from django.urls import path, include
from .views import *

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
    path("high_tasks_list/<int:list_id>/", list_detail_med_view, name="high_tasks"),
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
]
