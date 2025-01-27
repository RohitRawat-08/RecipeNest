from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,login ,logout

# Create your views here.

def LogIn(request):
    if request.method == "POST":
        u_name = request.POST['username']
        u_password= request.POST['password']

        user = authenticate(username = u_name, password = u_password)
        print(user)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            return HttpResponse("Invalid credentials")

    return render ( request , 'LogIn.html')



def new_registration(request):

    if request.method== "POST":
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        User_Name = request.POST['username']
        User_Email = request.POST['email']
        User_Password = request.POST['password']

        data = User.objects.create(first_name=f_name, last_name=l_name, username=User_Name,email=User_Email,password=User_Password)
        data.set_password(User_Password)
        data.save()

        return redirect("LogIn")


    return render (request , 'new_registration.html')


def LogOut(request):
    logout(request)
    return redirect('LogIn')