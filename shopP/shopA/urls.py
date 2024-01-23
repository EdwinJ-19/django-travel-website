from django.urls import path
from . import views 
from form.urls import *

urlpatterns=[
    path('',views.log_page,name='login'),
    path('register/',views.register, name='register'),
    path('main/',views.main, name='main'),
    path('travel/',views.book,name='travel'),
    path('about/',views.about,name='about'),
    path('logout/',views.out_page,name='out_page'),
    path('form/',views.form,name='form')
    # path('logout/',views.logout, name='logout')
]