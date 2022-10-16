from django.shortcuts import render

# Create your views here.

def skills(request):
    return render(request, 'personalAccount/skills.html')

def inventory(request):
    return render(request, 'personalAccount/inventory.html')

def account(request):
    return render(request, 'personalAccount/account.html')

def angar(request):
    return render(request, 'personalAccount/angar.html')

def repository(request):
    return render(request, 'personalAccount/repository.html')

def clan_repository(request):
    return render(request, 'personalAccount/clanRepository.html')

def character(request):
    return render(request, 'personalAccount/character.html')
