from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    race_type = (
        (1, 'Омоленианин (Красные)'),
        (2, 'Иррииец (Жёлтые)'),
        (3, 'Анид (Зелёные)'),
        (4, 'Медрамилл (Синие)'),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', "race")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        # fields = ('username', 'email', 'password1', 'password2')


