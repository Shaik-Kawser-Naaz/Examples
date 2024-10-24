from django.urls import path
from result import views

urlpatterns=[
    path('sem5/<str:rollno>',views.student,name='rpage'),
]