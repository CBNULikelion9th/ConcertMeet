from django import forms
from .models import Post
from .models import Comment
from .models import Review

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('message',)