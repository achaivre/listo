from django.urls import path
from .views import (
    LoginView_ToDo,
    CreateUserPage,
    AllTasks,
    Completed_View,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    HighPriority,
    LowPriority,
    MediumPriority,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("accounts/login/", LoginView_ToDo.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", CreateUserPage.as_view(), name="register"),
    # Show Tasks Pages
    path("", AllTasks.as_view(), name="all_tasks"),
    path("completed-tasks/", Completed_View.as_view(), name="completed_tasks"),
    path("high-priority-tasks/", HighPriority.as_view(), name="high_tasks"),
    path("med-priority-tasks/", MediumPriority.as_view(), name="medium_tasks"),
    path("low-priority-tasks/", LowPriority.as_view(), name="low_tasks"),
    # Task Creation/Editing Pages
    path("task-create/", TaskCreate.as_view(), name="create_task"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="delete_task"),
]
