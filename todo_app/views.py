from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 
from todo_app.models import Todo
# Create your views here.


ORDER = {
    "0": 'created_at',
    "1": '-created_at'
}


def index(request):
    search = request.GET.get('todoSearch')
    completed = request.GET.get("completed")
    order = request.GET.get('order')
    all_todos = Todo.objects.all()
    if search != None:
        all_todos = all_todos.filter(title__icontains=search)
    if completed != None:
        all_todos = all_todos.filter(completed=completed)
    if order != None:
        value = ORDER.get(order)
        all_todos = all_todos.order_by(value)

    context = {
        "todos": all_todos
    }
    return render(request, 'index.html', context)

def add_todo(request):
    if request.method == "GET":
        return HttpResponse('Invalid Method')
    else:
        todo_input = request.POST['todoInput']
        new_todo = Todo(title=todo_input)
        new_todo.save()
        print(new_todo.id)
        return redirect('todo_index')

def detail_view(request, todoId):
    a = Todo.objects.get(id=todoId)
    context = {
        'title': a.title,
        'completed': a.completed,
        'created_at': a.created_at,
        'updated_at': a.updated_at
    }
    return JsonResponse(context)

def delete_todo(request, todo_id):
    if request.method == "GET":
        return HttpResponse('Invalid Method')
    else:
        todo_object = Todo.objects.get(id=todo_id)
        todo_object.delete()
        return redirect('todo_index')

def mark_todo(request, todo_id):
    if request.method == "GET":
        return HttpResponse('Invalid Method')
    else:
        todo_object = Todo.objects.get(id=todo_id)
        todo_object.completed = True 
        todo_object.save()
        return redirect('todo_index')


def test(request):
    return HttpResponse('Testing Django in production')