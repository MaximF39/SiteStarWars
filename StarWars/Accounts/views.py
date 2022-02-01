from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Accounts.forms import RegisterUserForm, LoginUserForm
from Accounts.utils import DataMixin
from django.contrib.auth import logout
from django.shortcuts import redirect


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'Accounts/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'Accounts/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')

def logout_user(request):
    logout(request)
    return redirect('main')

# class PlayerCreateView(generics.CreateAPIView):
#     serializer_class = PlayerDetailSerializers
#     permission_classes = (IsAdminUser,)
#
# class PlayerListView(generics.ListAPIView):
#     serializer_class = PlayerListSerializers
#     queryset = Player.objects.all()
#     permission_classes = (IsAdminUser,)
#
# class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PlayerDetailSerializers
#     queryset = Player.objects.all()
#     permission_classes = (IsOwnerOrReadOnly, IsAdminUser)
