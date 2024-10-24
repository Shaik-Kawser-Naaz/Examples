from django.urls import path
from ex1 import views
urlpatterns=[
    path('f1',views.url1),
    path('f2',views.url2)
]