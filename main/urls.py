from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="Homepage"),
    path('about', views.about, name="About"),
    path('message', views.message, name="Feedback"),
]