from django.urls import path
from app1 import views
urlpatterns=[
    path('<str:name1>/<str:name2>',views.func1)

]