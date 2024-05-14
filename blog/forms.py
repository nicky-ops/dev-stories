from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']