from django.shortcuts import render
from shopA.views import *

def form(request):
    
    return render(request,'form.html')