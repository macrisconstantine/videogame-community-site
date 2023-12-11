from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def homepage(request):
#     return render(request, "main/home.html")

def homepage(request):
    return HttpResponse("This is the homepage!")