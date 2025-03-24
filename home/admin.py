from django.contrib import admin

from . models import TaskGroup, Task
# Register your models here.

class TaskInLine(admin.TabularInline):
    model = Task

class TaskGroupAdmin(admin.ModelAdmin):
    model = TaskGroup
    inlines = [TaskInLine,]
    
class TaskAdmin(admin.ModelAdmin):
    model = Task
    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'due_date'), 'taskgroup'
            ]
        })
    ]

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)
