from django.shortcuts import render, redirect


def registration(request):
    return render(request, 'Main/register.html')

def download(request):
    return render(request, 'Main/download.html')

def main(request):
    return render(request, 'Main/main.html')

def redirect_main(request):
    return redirect('/main')

def faq(request):
    return render(request, 'Main/faq.html')

def news(request):
    return render(request, 'Main/news.html')

def top(request):
    return render(request, 'Main/top.html')