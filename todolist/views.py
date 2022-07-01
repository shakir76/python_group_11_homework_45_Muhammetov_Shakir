from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from todolist.forms import TaskForm
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
        form = TaskForm()
        return render(request, "create.html", {'statuses': STATUS_CODE, "form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.cleaned_data.get("task")
            status = form.cleaned_data.get("status")
            created_at = form.cleaned_data.get("created_at")
            description = form.cleaned_data.get("description")
            new_task = Task.objects.create(task=task, status=status, created_at=created_at, description=description)
            return redirect("view", pk=new_task.pk)
        return render("create.html", {"form": form})


def update_task(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            "task": tasks.task,
            "status": tasks.status,
            "description": tasks.description,
            "created_at": tasks.created_at
        })
        return render(request, "update.html", {'form': form, 'statuses': STATUS_CODE})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            tasks.task = form.cleaned_data.get("task")
            tasks.status = form.cleaned_data.get("status")
            tasks.created_at = form.cleaned_data.get("created_at")
            tasks.description = form.cleaned_data.get("description")
            tasks.save()
            return redirect("view", pk=tasks.pk)
        return render(request, "update.html", {'form': form, 'statuses': STATUS_CODE})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        pass
        return render(request, "delete.html", {"task": task})
    else:
        task.delete()
        return redirect("index")
