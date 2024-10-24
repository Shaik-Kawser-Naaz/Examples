from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request):
    d={
        'place':'kurnool'
    }
    return render(request,'home.html',d)

def func2(request):
    d1={'name':"john",'age':10,'status':'elgible'}
    return render(request,'vote.html',d1)

def func3(request):
    d2={'movies':[
        {'name':'salaar','year':2004},
        {'name':'mirchi','year':2006},
        {'name':'bahubali','year':2008}]}
    return render(request,'movies.html',d2)