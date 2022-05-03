from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', views.clinic, name="Homepage"),
    path('about', views.about, name="About"),
    path('message', views.message, name="Feedback"),
    path('registration', views.registration, name="Registration"),
    path('authorization', LoginUser.as_view(), name="Authorization"),
    path('logout/', logout_user, name='logout'),
    path('clinic', views.clinic, name="Clinic"),
    path('personpage', views.personpage, name="Personpage"),

    path('userinfo', UserInfo.as_view(), name="Userinfo"),
    path('register', RegisterUser.as_view(), name="Register"),



]