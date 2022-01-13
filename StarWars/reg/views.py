from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


class RegisterUser(DataMixin, CreateVie):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "reg/register.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.
        c_def = self.get_user_context(title='Регситрация')