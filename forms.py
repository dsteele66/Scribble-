from django import forms
from django.db.models import fields
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'title', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body', 'Post')
        