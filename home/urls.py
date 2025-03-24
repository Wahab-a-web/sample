from django.urls import path

from .views import index, TaskListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    #the url, function name, name for a specific url
    path('', index, name='index'),
    #path('task-list', task_list, name='task-list') ,
    path('task-list', TaskListView.as_view(), name='task-list'),
    path('add', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>', TaskUpdateView.as_view(), name="task-update")
]

app_name = "home"

