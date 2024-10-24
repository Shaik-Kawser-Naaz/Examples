from django.urls import path
from page import views

urlpatterns=[
    path('home',views.home,name='HomePage'),
    path('about',views.about,name='AboutPage'),
    path('contact',views.contact,name='ContactPage'),
    path('help',views.help,name='HelpPage'),
    path('ispalin/<str:sname>',views.func1,name='palindromepage'),
    path('evenorodd/<int:num>',views.func2,name='evenorodd'),


]