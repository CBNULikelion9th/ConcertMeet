from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from .models import Review


class UserForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    # getGender = [('man'), ('woman')]
    # gender = forms.CharField(label='gender', widget=forms.RadioSelect(choices=getGender))
    # getInterests = [('Ballad'), ('hiphop'), ('idol')]
    # interests = forms.MultipleChoiceField()

    class Meta:
        model = User
        fields = ("username", "name", "email", "phone")


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