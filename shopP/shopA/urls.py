from django.urls import path
from . import views 
from form.urls import *

urlpatterns=[
    path('',views.log_page,name='login'),
    path('register/',views.register, name='register'),
    path('main/',views.main, name='main'),
    path('travel-page/',views.travel_page,name='travel-page'),
    path('travel/',views.travel,name='travel'),
    path('about/',views.about,name='about'),
    path('logout/',views.out_page,name='out_page'),
    path('form/',views.form,name='form'),
    # path('search',views.search,name='search')
    # path('logout/',views.logout, name='logout')
]