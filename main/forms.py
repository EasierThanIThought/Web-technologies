from .models import Feedback
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

