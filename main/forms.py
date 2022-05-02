from .models import *
from django import forms
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class FeedBackForm(ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ["name", "feedback"]
#         widgets = {
#             "name": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Ваш никнейм'
#             }),
#             "feedback": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Отзыв...'
#             }),
#         }
#
#
# class RegisterForm(ModelForm):
#     class Meta:
#         model = Patient
#         fields = ["name", "passport"]
#         widgets = {
#             "name": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Ваше имя'
#             }),
#             "passport": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Пароль'
#             }),
#         }
#
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')