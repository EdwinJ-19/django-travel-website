from django.urls import path
from . import views 

urlpatterns=[
    path('',views.log,name='log'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    # path('main/',views.main, name='main'),
    path('logout/',views.logout, name='logout')
]