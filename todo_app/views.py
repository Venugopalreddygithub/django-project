from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 

# Create your views here.
def index(request):
    html = '''
    <h1>Hello Django</h1>
    <p>This is an html Response</p>
    '''
    return HttpResponse(html)

def bye(request):
    dict_a = {
        "title": "Think and Grow Rich",
        "author": "Nepoleon Hill",
    }
    return JsonResponse(dict_a)

def hello(request):
    return render(request, 'index.html')