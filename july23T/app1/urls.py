from django.urls import path
from app1 import views
urlpatterns=[
    path('route1',views.func1,name='p1'),
    path('check',views.func2,name='p2'),
    path('list',views.func3,name='p3'),
]