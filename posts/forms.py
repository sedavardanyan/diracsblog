from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=250)
    body = forms.TextInput()

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
