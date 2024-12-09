import django
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, DirectMessage, Skill


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class AddSkillForm(forms.Form):
    skill_name = forms.CharField(max_length=200, label="Add Skill", required=True)

    def clean_skill_name(self):
        skill_name = self.cleaned_data.get("skill_name").strip()
        if not skill_name:
            raise forms.ValidationError("Skill name cannot be empty.")
        return skill_name


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
