from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request):
    return HttpResponse("Hey dude how are you")