from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User


def log(request):
    return render(request,'log.html')

def main(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request,'main.html',param)
    else:
        return redirect('register.html')

def register(request):
    if request.method == 'POST':
        e_mail = request.POST.get('email')
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        a_pwd = request.POST.get('a_pwd')

        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username Already Exists')
        else:
            user = User(email=e_mail,username=uname,password=pwd,again_password=a_pwd)
            user.save()
            return redirect('log.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname,password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('main.html')
        else:
            return HttpResponse('Please Enter your valid username or password!')
    else:
        return render(request,'log.html')
    
def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('log.html')
    return redirect('log.html')