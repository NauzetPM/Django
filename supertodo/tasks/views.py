from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm
from .models import Task


def home(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})


def task_details(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/details.html', {'task': task})


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:home')
    else:
        form = AddTaskForm()
    return render(request, 'tasks/add_task.html', dict(form=form))


def task_filtered_list(request, filter):
    if filter == 'Pending':
        tasks = Task.objects.filter(done=False)
    elif filter == 'Done':
        tasks = Task.objects.filter(done=True)
    else:
        tasks = Task.objects.none()

    context = {'tasks': tasks, 'filter': filter}
    return render(request, 'tasks/filter_list.html', context)


def toggle_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.done = not task.done
    task.save()
    return redirect('tasks:home')


def edit_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)

    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:home')
    else:
        form = AddTaskForm(instance=task)

    return render(request, 'tasks/task/edit_task.html', {'form': form})


def delete_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.delete()
    return redirect('tasks:home')
