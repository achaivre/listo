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
    Sp_LoginView_ToDo,
    Sp_CreateUserPage,
    Sp_AllTasks,
    Sp_Completed_View,
    Sp_TaskCreate,
    Sp_TaskUpdate,
    Sp_TaskDelete,
    Sp_HighPriority,
    Sp_LowPriority,
    Sp_MediumPriority,
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
    # spanish urls
    # spanish urls
    path("accounts/slogin/", Sp_LoginView_ToDo.as_view(), name="slogin"),
    path("slogout/", LogoutView.as_view(next_page="login"), name="slogout"),
    path("sregister/", CreateUserPage.as_view(), name="sregister"),
    # Show Tasks Pages
    path("", AllTasks.as_view(), name="all_tasks"),
    path("scompleted-tasks/", Sp_Completed_View.as_view(), name="scompleted_tasks"),
    path("shigh-priority-tasks/", Sp_HighPriority.as_view(), name="shigh_tasks"),
    path("smed-priority-tasks/", Sp_MediumPriority.as_view(), name="smedium_tasks"),
    path("slow-priority-tasks/", Sp_LowPriority.as_view(), name="slow_tasks"),
    # Task Creation/Editing Pages
    path("stask-create/", Sp_TaskCreate.as_view(), name="screate_task"),
    path("stask-update/<int:pk>/", Sp_TaskUpdate.as_view(), name="supdate_task"),
    path("stask-delete/<int:pk>/", Sp_TaskDelete.as_view(), name="sdelete_task"),
]
