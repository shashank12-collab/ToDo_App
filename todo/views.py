from django.shortcuts import render
from todoss.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed = True)
    context= {
        'tasks' : tasks,
        'completed_task':completed_tasks
    }
    return render(request ,'home.html',context)