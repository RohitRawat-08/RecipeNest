from django.urls import path
from . import views

urlpatterns = [
    path('',views.LogIn , name="LogIn"),
    path('new_registration',views.new_registration , name="new_registration"),
    path("logout",views.LogOut,name='LogOut'),
    
]