from django.contrib import admin

# Register your models here.
from todolist.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'status', 'created_at']
    list_display_links = ['task']
    list_filter = ['status']
    search_fields = ['task']
    fields = ['task', 'status', 'created_at']


admin.site.register(Task, TaskAdmin)
