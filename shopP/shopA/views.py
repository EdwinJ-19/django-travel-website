from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from shopA.models import crud
# from django.db.models import Q
from .models import *
from form.models import form

def form_page(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        date_transportation = request.POST.get('date_transportation')
        time_transportation = request.POST.get('time_transportation')
        passenger = request.POST.get('passenger')
        vehicle = request.POST.get('vehicle')
        description = request.POST.get('description')
        heading = request.POST.get('head')

        form1 = form.objects.filter(first_name=first_name)

        if form1.exists():
            messages.error(request,'Form has already been filled!')
            return redirect('form')

        form1 = form.objects.create(first_name=first_name,last_name=last_name,phone=phone,date_transportation=date_transportation,time_transportation=time_transportation,passenger=passenger,vehicle=vehicle,description=description)
        form1.save()

        messages.success(request,'Form is filled!')

        return redirect('payment')

        # if form.objects.filter(first_name = first_name).exists():
        #     messages.error(request,'Form Has been Filled')
        #     return redirect('form.html')
        # else:
        #     form = form.objects.create(first_name=first_name,last_name=last_name,phone=phone,date_transportation=date_transportation,time_transportation=time_transportation,passenger=passenger,sedan=sedan,bus=bus,suv=suv,van=van,other=other,description=description)
        #     form.save()
        #     messages.success(request,'Form Has been Filled!')
        #     return redirect('travel-page')

    return render(request,'form.html')

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
    # data = crud.objects.all()
    # if request.method =='GET':
    #     st=request.GET.get('searchname')
    #     if st!=None:
    #         data=crud.objects.filter(head=st)
    #         return render(request,'travel-page.html',{'data':data})
    return render(request,'main.html')

def travel(request):
    data = crud.objects.all()
    return render(request,'travel.html',{'data':data})

def about(request):
    return render(request,'about.html')

def travel_page(request):
    data = crud.objects.all()
    if request.method =='GET':
        sn=request.GET.get('searchname')
        # lc=request.GET.get('location')
        # pr=request.GET.get('price')
        if sn!=None:
            data=crud.objects.filter(head=sn)
            return render(request,'travel.html',{'data':data})
    return render(request,'travel-page.html',{'data':data})

def payment(request):
    data = crud.objects.all()
    if request.method == 'POST':
        heading = request.POST.get('head')
        data = crud.objects.filter(head = heading)
    return render(request,'payment.html',{'data':data})

 
# def search(request):
    
#     if request.method =="POST":
#         searchvalue = request.POST['search']
#         data = crud.object.filter(Q(head__icontains = searchvalue)| Q(sentence__icontains = searchvalue) | Q(destination__icontains = searchvalue) | Q(nearby__icontains = searchvalue)| Q(attraction__icontains = searchvalue) | Q(transportation__icontains = searchvalue) | Q(price__icontains = searchvalue)) 
#         return render(request,'travel.html',{'data':data},{'searchvalue':searchvalue})
#     else:
#         data = crud.objects.all()
#         return render(request,'travel-page.html',{'data':data})