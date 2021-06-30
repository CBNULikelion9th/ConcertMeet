from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class UserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    profpic = forms.ImageField(required=False)
    gender = forms.CharField(required=False)
    interests = forms.CharField(required=False)
    class Meta:
        model = UserInfo
        fields = ('username', 'name', 'email','phone', 'date_of_birth', 'gender', 'interests')

class FollowForm(forms.ModelForm):
    class Meta:
        model: Follow
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('message',)