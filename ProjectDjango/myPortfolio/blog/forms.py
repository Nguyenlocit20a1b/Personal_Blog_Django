from django import forms
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'blog_img' , 'body' ]