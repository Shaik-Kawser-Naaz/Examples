from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request,name1,name2):
    return HttpResponse(f"<p>{name1} : Johnny Johnny<br> {name2} : Yes pappa!<br>{name1} : Eating Sugar??<br>{name2} : No pappa!<br>{name1} : Telling lies?!<br>{name2} : No pappa!<br>{name1} : Open your mouth?<br>{name2} : Haha Haha.....</p>")