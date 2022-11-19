from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from LoginApp.models import UserProFile


class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email address', required=True,)

    class Meta:
        model = User
        fields = ('username', 'password1','password2','email')

class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password')


class ProPicForm(forms.ModelForm):
    class Meta:
        model = UserProFile
        fields = ['proPic']








        
