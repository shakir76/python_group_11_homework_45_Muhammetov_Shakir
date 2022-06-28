from django.urls import path

from todolist.views import index, create_task, task_view

urlpatterns = [
    path('', index, name="index"),
    path('add/', create_task, name="add"),
    path('task/<int:pk>/', task_view, name="view")
]
