from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm

from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('-date_added')
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            #print(form)
        return redirect('/')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/main.html', context)


def update_task(request, pk):
    #task = get_object_or_404(pk=pk)
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', {'task': task})

