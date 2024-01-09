from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


def log(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Username')
            return redirect('login')
        
        user = authenticate(username = username,password = password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('login')
        
        else:
            login(request, user)
            return redirect('main')


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

        user = User.objects.create(first_name = first_name,email = email,username=username,password=password)
        
        user.set_password(password)
        user.save()

        messages.info(request,'Account Created Successfully!')

        return redirect('register')
    return render(request,'register.html')
# def register(request):
#     form:UserForm
#     if request.method=="POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Registration Successfull!')
#             return redirect('/log')
#         else:
#             return render(request,'register.html',{'form':form})
#     else:
#         form = UserForm()
#         return render(request,'register.html',{'form':form})
    
# def login(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     else:
#         if request.method == "POST":
#             username = request.POST.get('uname')
#             password = request.POST.get('pwd')
#             user = auth.authenticate(username=username,password=password)

#             if user is not None:
#                 auth.login(request,user)
#             else:
#                 messages.error(request,"Invalid Username & Passsword")
#                 return redirect('/log')
#         else:
#             return render(request,'log')

def main(request):
    return render(request,'main.html')

def book(request):
    return render(request,'travel.html')

def about(request):
    return render(request,'about.html')