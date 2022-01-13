from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def registration(request):
    return render(request, 'home/registration.html')