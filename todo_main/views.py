from django.shortcuts import render
from todos.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    uncompleted_tasks = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'uncompleted_tasks': uncompleted_tasks
    }
    return render(request, 'home.html', context)