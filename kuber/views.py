from django.shortcuts import render
from prices.models import objects


def index(request):
    return render(request,'index.html',{ "obj" : objects.objects.all() })


def form(request):
    return render(request,'form.html')

def about(request):
    return render(request,'about.html')