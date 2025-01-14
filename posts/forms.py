from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "image",
            "caption"
        ]

class CommentCreatForm(forms.ModelForm):

    class Meta:
        model= Comment
        fields = {
            'text',
        }
        