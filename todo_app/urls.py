from django.contrib import admin
from django.urls import path
from todo_app.views import index, add_todo, detail_view, delete_todo, mark_todo, test 
urlpatterns = [
    path('', index, name='todo_index'),
    path('add-todo/', add_todo, name='add_todo'),
    path('detail-view/<int:todoId>/', detail_view, name='detail_view'),
    path('delete-todo/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('mark-todo/<int:todo_id>/', mark_todo, name='mark_todo'),
    path('test/', test, name='test'),
]