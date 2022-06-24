from django.urls import path

from todolist.views import index, create_task

urlpatterns = [
    path('', index),
    path('add/', create_task)
]
