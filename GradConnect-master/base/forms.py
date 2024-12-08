import django
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, DirectMessage


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']

class DirectMessageForm(forms.ModelForm):
    class Meta:
        model = DirectMessage
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your message here...'})
        }
