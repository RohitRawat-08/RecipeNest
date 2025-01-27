from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home , name="home"),
    path('add_recipe',views.add_recipe , name="add_recipe"),
    path('your_recipe',views.your_recipe , name="your_recipe"),
    path('edit/<int:id>',views.edit , name="edit"),
    path('delete/<int:id>',views.delete , name="delete"),
    path('Profile',views.Profile , name="Profile"),
]