from .models import *
from django import forms
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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

class UserInfoForm(ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    passport = forms.CharField(label='Passport', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone_number = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'form-input'}))
    #user_id=forms.CharField(initial=request.user)

    class Meta:
        model = Patient
        fields = ['name', 'surname', 'passport', 'phone_number', 'birth']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Patient
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
