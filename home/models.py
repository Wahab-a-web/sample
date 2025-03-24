from django.db import models
from django.urls import reverse 

# Create your models here.

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    # in java, it would be public class Task implements models.Model 
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
        #required to set the due date
    taskgroup = models.ForeignKey(
        TaskGroup,
        on_delete=models.SET_NULL,
        null=True,
        related_name='task_detail'
        )

    def get_absolute_url(self):
        return reverse('home:task-detail', args=[self.pk])
        #this will return /home/task/1
        #so <a href="{{ task.get_absolute_url() }}>Task</a>"

    def __str__(self):
        return f'{self.name} due on {self.due_date}'
    
    class Meta:
        ordering=['due_date'] #order by ascending order. for descending, do -due_date
        unique_together = ['due_date', 'name'] #all names will be w same due date
        verbose_name = 'task'
        verbose_name_plural = 'tasks'



