from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.root, name="main"),
    path("tasklist/", v.TaskList.as_view(), name="task_list"),
    path("task/<int:pk>", v.TaskDetail.as_view(), name="task_detail"),
]
