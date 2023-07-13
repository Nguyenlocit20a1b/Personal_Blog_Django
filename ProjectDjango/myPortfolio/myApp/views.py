from django.shortcuts import render
from .models import Portfolio , myPodcard

def home(request):
    return render (request , 'homepage.html')

def about(request):
    return render (request , 'about.html')

def portfolio(request):
    context = {
        'portfolio' : Portfolio.objects.all()
    }
    return render (request , 'portfolio.html', context)

   
def contact(request):
    return render (request , 'contact.html')

def getPodcard(request):
    context = {
        'podcard': myPodcard.objects.all()
    }
    return render (request , 'podcard.html' , context)