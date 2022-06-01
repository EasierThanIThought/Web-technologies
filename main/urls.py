from django.urls import path, include
from . import views
from .views import *
from django.views.i18n import JavaScriptCatalog
urlpatterns = [
    path('', views.clinic, name="Homepage"),
    path('authorization', LoginUser.as_view(), name="Authorization"),
    path('logout/', logout_user, name='logout'),
    path('clinic', views.clinic, name="Clinic"),
    path('personpage', views.personpage, name="Personpage"),
    #path('personpage', PersonPage.as_view(), name="Personpage"),


   # path('<int:pk>', PatientDetail.as_view(), name="patient_detail" ),
    path('appointment', AppointmentInfo.as_view(), name="Appointment"),
    path('appointment_info', AppointmentListView.as_view(), name="Appointment_Info"),


    path('<int:pk>', UserInfo.as_view(), name="Userinfo"),
    path('register', RegisterUser.as_view(), name="Register"),
    path('doctor_info', ServiceListView.as_view(), name="Doctor"),

    path('mRecord', MRecordsListView.as_view(), name="MRecord"),



]