from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("toggle/<int:task_id>/", views.toggle_task),
    path("delete/<int:task_id>/", views.delete_task),
]