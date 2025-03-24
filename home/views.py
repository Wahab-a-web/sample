from django.shortcuts import render

# Create your views here.
#this is new
from django.http import HttpResponse

#this is added for models 
from .models import Task, TaskGroup
from .forms import TaskForm
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taskgroups'] = TaskGroup.objects.all()
        context['form'] = TaskForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_date(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_detail.html'
    # template to be used by default is called <model>_form.html
    form_class = TaskForm
    # we can use the created TaskForm so we can leverage the custom widgets

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    # template to be used by default is called <model>_form.html
    template_name = 'task_detail.html'
    # use TaskForm to leverage custom widgets defined (optional)        

def task_detail(request, pk):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.post)

        if form.is_valid():
            t = Task()
            t.name = request.POST.get('name')
            t.due_date = request.POST.get('due_date')
            t.taskgroup = TaskGroup.objects.get(
                pk=request.POST.get('taskgroup')
            )
            t.save()

    ctx = {
        "object": Task.objects.get(pk=pk),
        "taskgroups": TaskGroup.objects.all(),
        "form": form
    }

    return render(request, 'task_detail.html', ctx)

def index(request):
    return HttpResponse('Hello world')
