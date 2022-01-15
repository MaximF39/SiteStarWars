from django.shortcuts import render

def registration(request):
    return render(request, 'reg/register.html')