from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 
from todo_app.models import Todo
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos
    }
    return render(request, 'index.html', context)