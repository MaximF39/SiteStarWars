from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from reg.forms import RegisterUserForm, LoginUserForm
from reg.utils import DataMixin


def registration(request):
    context = {'title': 'Страница регистрации'}
    return render(request, 'reg/register.html', context=context)

def main(request):
    return render(request, 'reg/main.html')

def base(request):
    return render(request, 'base/base.html')

def redirect_main(request):
    response = redirect('/main')
    return response

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'reg/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')

def logout_user(request):
    logout(request)
    return redirect('main')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'reg/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')
