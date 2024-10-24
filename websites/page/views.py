from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def help(request):
    return redirect('AboutPage')
def func1(request,sname):
    res=(sname==sname[::-1])
    d={'result':res}
    return render(request,'palindrome.html',d)
def func2(request,num):
    res1=(num%2==0)
    b={'result1':res1}
    return render(request,'evenodd.html',b)
 def func3(request,num1):
    res2=  