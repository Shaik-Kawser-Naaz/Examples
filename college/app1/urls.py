from django.urls import path
from app1 import views
 
urlpatterns=[
    path('home',views.func1,name="hp")
]