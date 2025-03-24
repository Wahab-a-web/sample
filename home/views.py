from django.shortcuts import render

# Create your views here.
#this is new
from django.http import HttpResponse

#this is added for models 
from.models import Task
from django.views.generic.list import ListView 

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

def index(request):
    return HttpResponse('Hello world')

#new lesson

def task_list(request):
    '''
    ctx = {
        "tasks": [
            'Task 1',
            'Task 2',
            'Task 3',
            'Task 4',
            'Task 5'
        ]
    }
    return render(request, 'task_list.html', ctx)
    '''
    tasks = Task.objects.all()
    ctx = { "tasks": tasks }

    return render(request, 'task_list.html', ctx)

def task_detail(request, pk):
    ctx = { "task": Task.objects.get(pk=pk)}
    
    #return pk

    return render(request, 'task_detail.html', ctx)


