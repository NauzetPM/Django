from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'done']
    prepopulated_fields = {'slug': ['name']}
