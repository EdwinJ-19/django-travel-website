from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from shopA.models import crud
# from form.models import *


def log_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid Username')
            return redirect('login')
        
        user = authenticate(username = username, password=password)

        if user is None:
            messages.error(request,'Password Or Username is not Correct!')
            return redirect('login')
        
        else:
            login(request,user)
            return redirect ('main')

    return render(request,'log.html')

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('e_mail')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'Username Already Taken')
            return redirect('register')

        user = User.objects.create(first_name=first_name,email=email,username=username)
        user.set_password(password)
        user.save()

        messages.info(request,'Account Created Successfully!')

        return redirect('register')
    return render(request,'register.html')

def out_page(request):
    logout(request)
    return render(request,'logout.html')

def main(request):
    data = crud.objects.all()
    if request.method == 'GET':
        st=request.GET.get('searchname')
        if st!=None:
            data =crud.objects.filter(head__contains=st)
            return render(request,'travel-page.html',{'data':data})
    return render(request,'main.html',{'data':data})

def book(request):
    data=crud.objects.all()
    return render(request,'travel.html',{'data':data})

def about(request):
    return render(request,'about.html')

def travel_page(request):
    data = crud.objects.all()
    if request.method == 'GET':
        st=request.GET.get('searchname')
        loc=request.GET.get('location')
        price=request.GET.get('price')
        if st!=None:
            data=crud.objects.filter(head__contains=st)
            data=crud.objects.filter(destination__contains=loc)
            data=crud.objects.filter(price__contains= price)
            return render(request,'travel.html',{'data':data})
    return render(request,'travel-page.html',{'data':data})

# def form(request):
#     return render(request,'form.html')