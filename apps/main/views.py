from django.shortcuts import render, redirect


def registration(request):
    return render(request, 'main/register.html')

def download(request):
    return render(request, 'main/download.html')

def main(request):
    return render(request, 'main/main.html')

def redirect_main(request):
    return redirect('/main')

def faq(request):
    return render(request, 'main/faq.html')

def news(request):
    return render(request, 'main/news.html')

def top(request):
    return render(request, 'main/top.html')
