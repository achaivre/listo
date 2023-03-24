from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("accounts/login/", LoginView_ToDo.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", CreateUserPage.as_view(), name="register"),
    # Show List Pages
    path("", AllLists.as_view(), name="home"),
    path("list-create/", ListCreate.as_view(), name="create_list"),
    path("list-update/<int:pk>/", ListUpdate.as_view(), name="update_list"),
    path("list-delete/<int:pk>/", ListDelete.as_view(), name="delete_list"),
    # Show Tasks Pages
    path("list_detail/<int:pk>", AllTasks.as_view(), name="all_tasks"),
    path("completed-tasks/<int:pk>/", Completed_View.as_view(), name="completed_tasks"),
    path("high-priority-tasks/<int:pk>/", HighPriority.as_view(), name="high_tasks"),
    path("med-priority-tasks/<int:pk>/", MediumPriority.as_view(), name="medium_tasks"),
    path("low-priority-tasks/<int:pk>", LowPriority.as_view(), name="low_tasks"),
    # Task Creation/Editing Pages
    path("task-create/", TaskCreate.as_view(), name="create_task"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="delete_task"),
]
