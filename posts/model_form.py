# Django

from django.forms import ModelForm

# Models
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'profile', 'title', 'photo']