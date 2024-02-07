from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from shopA.models import crud
# from django.db.models import Q
from .models import *
from form.models import form
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

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

# def payment(request):
#     data = crud.objects.all()
#     # if request.method == 'POST':
#     #     heading = request.POST.get('head')
#     #     data = crud.objects.filter(head = heading)
#     return render(request,'payment.html',{'data':data})

 
# def search(request):
    
#     if request.method =="POST":
#         searchvalue = request.POST['search']
#         data = crud.object.filter(Q(head__icontains = searchvalue)| Q(sentence__icontains = searchvalue) | Q(destination__icontains = searchvalue) | Q(nearby__icontains = searchvalue)| Q(attraction__icontains = searchvalue) | Q(transportation__icontains = searchvalue) | Q(price__icontains = searchvalue)) 
#         return render(request,'travel.html',{'data':data},{'searchvalue':searchvalue})
#     else:
#         data = crud.objects.all()
#         return render(request,'travel-page.html',{'data':data})

razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def payment(request):
    currency = 'INR'
    amount = 20000
	# Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
                                                    payment_capture='0'))

    data = crud.objects.all()
	# order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
	# we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'payment.html', {'data':data,'context':context})


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt

def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 20000
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					messages.info('Payment Successful!')
					return render(request, 'travel-page.html')
				except:

					# if there is an error while capturing payment.
					messages.error('Payment Failed, Please Try Again!')
					return render(request, 'payment.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()