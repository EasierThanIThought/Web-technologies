from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.clinic, name="Homepage"),
    path('about', views.about, name="About"),
    path('message', views.message, name="Feedback"),
    path('registration', views.registration, name="Registration"),
    path('authorization', views.authorization, name="Authorization"),

    path('clinic', views.clinic, name="Clinic"),
    path('personpage', views.personpage, name="Personpage"),

    path('register', views.register, name="Register"),



]