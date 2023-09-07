from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 
from todo_app.models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.get(id=1)
    print(todos)
    html = '''
    <h1>Hello Django</h1>
    <p>This is an html Response</p>
    <p>Todo: {}</P>
    '''.format(todos.title)
    return HttpResponse(html)

def bye(request):
    todos = Todo.objects.get(id=4)
    dict_a = {
        "title": todos.title
    }
    return JsonResponse(dict_a)

def hello(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos
    }
    return render(request, 'index.html', context)