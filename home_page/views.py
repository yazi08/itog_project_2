from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, FormView
from .forms import *
from .models import *


# def home_page(request):
#     return render(request, 'home_page/home_page.html')
"""Домашняя страница"""
class HomeDetailView(ListView):
    paginate_by = 3
    model = Blog
    template_name = "home_page/home_page.html"
    context_object_name = 'blog'

"""Регистрация"""
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('home_page')


"""Авторизация"""

class LoginUser(LoginView):
    form_class =AuthenticationForm
    template_name = 'register/authentication.html'

    """Перевод на страницу после авторизации"""
    def get_success_url(self):
        return reverse_lazy('client')


"""Страница клиента"""
def client(request):
    return render(request, 'client/client.html')


"""Разлогинить клиента"""
def logout_user(request):
    logout(request)
    return redirect('authentication')

class ContactFormView(FormView):
    template_name = 'bot/bot.html'
    form_class = SummClientForm
    success_url = reverse_lazy('botik')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.save()
        # a = subprocess.Popen([sys.executable, 'API.py'])
        # code = a.wait()
        # print(code)
        return super().form_valid(form)



def botik(request):
    f = SummClientItog.objects.all()
    x=f.values().first()['sum_client']
    print (x)

    # from subprocess import call
    # a = call(["python", "API.py"])
    # a = subprocess.Popen([sys.executable, 'API.py'])
    # code = a.wait()

    return render(request, "bot/bot_1.html",{'x':x})
