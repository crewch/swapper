from .models import Post
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "tasks"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "tasks": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }