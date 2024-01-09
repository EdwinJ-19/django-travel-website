from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib import auth

User = get_user_model()

def log(request):
    return render(request,'about.html')

def register(request):
    form:UserForm
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Successfull!')
            return redirect('/log')
        else:
            return render(request,'register.html',{'form':form})
    else:
        form = UserForm()
        return render(request,'register.html',{'form':form})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('uname')
            password = request.POST.get('pwd')
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
            else:
                messages.error(request,"Invalid Username & Passsword")
                return redirect('/log')
        else:
            return render(request,'log')

def main(request):
    return render(request,'main.html')

def book(request):
    return render(request,'travel.html')

def about(request):
    return render(request,'about.html')