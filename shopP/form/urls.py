from django.urls import path
from . import views 

urlpatterns=[
    path('form/',views.form,name='form')
    # path('logout/',views.logout, name='logout')
]