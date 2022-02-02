from .models import Feedback
from django.forms import ModelForm, TextInput, Textarea


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
