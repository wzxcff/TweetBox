from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from a_tweetbox.models import UserProfile, Tweet


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['email', 'password']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'What’s on your mind?', 'rows': 4, "style": "resize: none;"}),
        }
        labels = {
            'text': '',
        }