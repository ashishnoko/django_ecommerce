
from django.shortcuts import render


def index(request):
    return render(request,'pages/home/home.html')


    
def contact(request):
    return render(request,'pages/contact/contact.html')