from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User


class FeedBackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "feedback"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш никнейм'
            }),
            "feedback": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв...'
            }),
        }


class RegisterForm(ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "passport"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "passport": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }

