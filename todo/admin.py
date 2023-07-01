from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'status', 'created_date']
    list_filter = ['user', 'status']
    ordering = ['created_date']
