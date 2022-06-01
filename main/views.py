from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from .forms import *
from .models import *


# from .utils import *


class ServiceListView(ListView):
    model = Doctor
    template_name = 'main/doctor_info.html'
    queryset = Doctor.objects.all().order_by('name')


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'main/appointment_info.html'
    queryset = Appointment.objects.all().order_by('patient_id')


class MRecordsListView(ListView):
    model = MedicalCard
    template_name = 'main/medical_record.html'
    queryset = MedicalCard.objects.all().order_by('patient')


def personpage(request):
    appointments = Appointment.objects.all()

    context = {
        'appointments': appointments,
    }
    return render(request, "main/personpage.html", context=context)


def clinic(request):
    return render(request, "main/clinic.html")


def home(request):
    return render(request, "main/home.html")


class UserInfo(UpdateView):
    model = Patient
    form_class = UserInfoForm
    template_name = 'main/userinfo.html'
    success_url = reverse_lazy("Personpage")


class AppointmentInfo(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'main/appointment.html'
    success_url = reverse_lazy("Appointment_Info")


class PatientDetail(DetailView):
    model = Patient
    template_name = 'main/details_view.html'
    context_object_name = 'patient'


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


def medical_record(request):
    return render(request, "main/medical_record.html")
