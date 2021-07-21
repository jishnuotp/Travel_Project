from django.http import HttpResponse
from django.shortcuts import render

from .models import destination
from .models import team
# Create your views here.
def demo(request):
    fetch = destination.objects.all()
    obj = team.objects.all()
    return render(request,"index.html",{'result':fetch,'result2':obj})
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    obj=x + y
    return render(request,"result.html",{'res':obj})

