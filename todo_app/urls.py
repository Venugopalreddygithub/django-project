from django.contrib import admin
from django.urls import path
from todo_app.views import index, bye, hello

urlpatterns = [
    path('index/', index, name='index'),
    path('bye/', bye, name='bye'),
    path('hello/', hello, name='hello')
]