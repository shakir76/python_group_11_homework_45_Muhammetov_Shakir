from django.shortcuts import render

# Create your views here.
from todolist.models import Task, STATUS_CODE


def index(request):
    task = Task.objects.order_by("-created_at")
    context = {"tasks": task}
    return render(request, "index.html", context)


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
        return render(request, "task_view.html", context)
