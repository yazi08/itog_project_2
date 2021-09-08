from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, FormView, TemplateView
from .forms import *
from .models import *
# from strategy.API import *
# from strategy.bot import *

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
    success_url = reverse_lazy('client')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('client')

"""Авторизация"""

class LoginUser(LoginView):
    form_class =AuthenticationForm
    template_name = 'register/authentication.html'

    """Перевод на страницу после авторизации"""
    def get_success_url(self):
        return reverse_lazy('client')


"""Страница клиента"""
class ClientView(LoginRequiredMixin,TemplateView):
    template_name = "client/client.html"


# def client(request):
#         return render(request, 'client/client.html')


"""Разлогинить клиента"""
def logout_user(request):
    logout(request)
    return redirect('authentication')

class ContactFormView(LoginRequiredMixin,FormView):
    template_name = 'bot/bot.html'
    form_class = SummClientForm
    success_url = reverse_lazy('botik')

    def form_valid(self, form):

        form.instance.who_client = self.request.user
        form.save()


        return super().form_valid(form)


def botik(request):
    histor = HistoryClient.objects.all()
    f = SummClientItog.objects.all()
    x=f.values().last()['sum_client']
    print (x)
    import subprocess
    p = subprocess.Popen('py home_page/API.py')
    return render(request, "bot/bot_1.html",{'x':x,'histor':histor})


def exit(request):
    histor = HistoryClient.objects.all()
    import subprocess
    p = subprocess.Popen('py home_page/test.py')
    return render(request,"bot/bot_1.html",{'histor':histor})


def about(request):
     return render(request, 'home_page/o_nas.html')

def contacts(request):
    return render(request, 'home_page/contacts.html')



def history_table(request):

    context = {
        'posts': HistoryClient.objects.filter(who=request.user),

    }

    return render(request, 'history_table/history_table.html', context)