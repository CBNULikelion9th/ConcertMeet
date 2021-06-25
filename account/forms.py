from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username', 'name', 'email','phone', 'date_of_birth', 'gender', 'interest')

class FollowForm(forms.ModelForm):
    class Meta:
        model: Follow
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('message',)