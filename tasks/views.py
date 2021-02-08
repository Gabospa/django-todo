from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

from .models import Task


class TaskListView(ListView):
    
    template_name = 'index.html'
    queryset = Task.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class TaskDeleteView(DeleteView):

    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks:index')

def create(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        task = Task.objects.create(title=title)
        task.save()

    return redirect('tasks:index')


