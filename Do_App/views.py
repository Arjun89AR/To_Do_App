from django.shortcuts import render, redirect

from . models import Todo
from . forms import AddTaskForm

def index(request):
    tasks = Todo.objects.all()
    form  = AddTaskForm()
    
    
    #"context" refers to a dictionary-like object that holds variables and their values, which are then passed to a template for rendering. 
    # This allows dynamic data to be displayed within HTML templates without embedding complex logic directly into the template files.
    context = {
        'tasks':tasks, 
        'form':form
    }
    return render(request, 'index.html', context)

def addTask(request):
    
    form = AddTaskForm(request.POST) 
    
    if form.is_valid():
        form.save()
        
    return redirect('/')

def deleteTask(request, id):
    
    task = Todo.objects.get(pk = id)
    
    task.delete()
    
    
    return redirect('/')

def completedTask(request, id):
    
    task = Todo.objects.get(pk = id)
    
    task.completed = True
    task.save()
    
    return redirect('/')

def updatedTask(request, id):
    
    tasks= Todo.objects.get(pk=id)
    updateform = AddTaskForm(instance=tasks)
    
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {
        'updateform':updateform,
        'key':id,
        'task':Todo.objects.all()
    }
    
    return render(request, 'index.html', context)

def deleteAllCompleted(request):
    
    Todo.objects.filter(completed=True).delete()
    
    return redirect('/')


def deleteAll(request):
    task=Todo.objects.all().delete()
    
    return redirect('/')