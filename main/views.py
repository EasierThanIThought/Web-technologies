from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
#from .utils import *

def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def message(request):
    error = ''
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
        else:
            error = 'Форма заполнена неверно'
    form = FeedBackForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/message.html", context)


def registration(request):
    return render(request, "main/registration.html")


# def authorization(request):
#     return render(request, "main/authorization.html")


def personpage(request):
    return render(request, "main/personpage.html")


def clinic(request):
    return render(request, "main/clinic.html")


def home(request):
    return render(request, "main/home.html")


# def register(request):
#     error = ''
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Clinic')
#         else:
#             error = 'Форма заполнена неверно'
#     form = FeedBackForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request, "main/register.html", context)

class UserInfo(UpdateView):
    model=Patient
    form_class = UserInfoForm
    template_name = 'main/userinfo.html'
    success_url = reverse_lazy("Personpage")
    #
    # def get_user_context(self, **kwargs):
    #     context = kwargs
    #     return context
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Save")
    #     return dict(list(context.items()) + list(c_def.items()))
class PatientDetail(DetailView):
    model=Patient
    template_name='main/details_view.html'
    context_object_name='patient'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy("Personpage")

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign up")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("Homepage")

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/authorization.html'

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign in")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy("Personpage")


def logout_user(request):
    logout(request)
    return redirect("Authorization")


