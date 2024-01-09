from django.urls import path
from . import views 

urlpatterns=[
    path('',views.log,name='login'),
    path('register/',views.register, name='register'),
    path('main/',views.main, name='main'),
    path('travel/',views.book,name='travel'),
    path('about/',views.about,name='about'),
    # path('logout/',views.logout, name='logout')
]