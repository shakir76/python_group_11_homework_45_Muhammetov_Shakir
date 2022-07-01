from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from todolist.models import Task, STATUS_CODE


def index(request):
    task = Task.objects.order_by("-created_at")
    context = {"tasks": task}
    return render(request, "index.html", context)


def task_view(request, **kwargs):
    pk = kwargs.get("pk")
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_view.html", {'task': task})


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS_CODE})
    else:
        task = request.POST.get("task")
        status = request.POST.get("status")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        new_task = Task.objects.create(task=task, status=status, created_at=created_at, description=description)
        context = {"task": new_task}
        return redirect("view", pk=new_task.pk)


def update_task(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, "update.html", {'task': tasks, 'statuses': STATUS_CODE})
    else:
        tasks.task = request.POST.get("task")
        tasks.status = request.POST.get("status")
        tasks.created_at = request.POST.get("created_at")
        tasks.description = request.POST.get("description")
        tasks.save()
        return redirect("view", pk=tasks.pk)
