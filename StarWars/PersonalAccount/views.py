from django.shortcuts import render

# Create your views here.

def skills(request):
    return render(request, 'PersonalAccount/skills.html')

def inventory(request):
    return render(request, 'PersonalAccount/inventory.html')

def account(request):
    return render(request, 'PersonalAccount/account.html')

def angar(request):
    return render(request, 'PersonalAccount/angar.html')

def repository(request):
    return render(request, 'PersonalAccount/repository.html')

def clan_repository(request):
    return render(request, 'PersonalAccount/clanRepository.html')
