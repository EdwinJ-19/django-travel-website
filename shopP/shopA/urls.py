from django.urls import path
from . import views 
from payment.views import *


urlpatterns=[
    path('',views.main,name='main'),
    path('register/',views.register, name='register'),
    path('travel-page/',views.travel_page,name='travel-page'),
    path('travel/',views.travel,name='travel'),
    path('about/',views.about,name='about'),
    path('logout/',views.out_page,name='out_page'),
    path('form/',views.form_page,name='form'),
    path('payment/',views.payment,name='payment'),
    path('paymenthandler/',views.paymenthandler,name='paymenthandler'),
    path('login/',views.log_page,name='login')
    # path('search',views.search,name='search')
    # path('logout/',views.logout, name='logout')
]