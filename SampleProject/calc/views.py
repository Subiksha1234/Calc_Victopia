from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html",{"name":"Subikshaa"})

def add(request):
    num1 = int(request.GET.get('num1', 0))
    num2 = int(request.GET.get('num2', 0))
    result = num1 + num2
    return render(request, "result.html", {"result": result})

