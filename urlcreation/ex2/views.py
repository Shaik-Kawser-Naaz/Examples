from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def url1(request):
    return HttpResponse("Im from app2 and url1")
def url2(request):
    return HttpResponse("Im from app2 and url2")