from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title','content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)

class PostDeclareForm(forms.ModelForm):
    class Meta:
        model = PostDeclaration
        fields = ('message',)

class CommentDeclareForm(forms.ModelForm):
    class Meta:
        model = CommentDeclaration
        fields = ('message',)