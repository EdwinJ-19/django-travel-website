from django.shortcuts import render
from shopA.views import *

def form(request):
    data = request.POST
    return render(request,'form.html')