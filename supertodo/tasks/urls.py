from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<task_slug>/', views.task_details, name='task-details'),
    path('add_task/', views.add_task, name='add-task'),
    path('<str:filter>/', views.task_filtered_list, name='task-filtered-list'),
    path('task/<task_slug>/edit/', views.edit_task, name='edit-task'),
    path('task/<task_slug>/delete/', views.delete_task, name='delete-task'),
    path('task/<task_slug>/toggle/', views.toggle_task, name='toggle-task'),
]
