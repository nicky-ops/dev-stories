from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    """
    form to authenticate users
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """
    Form for users to register their account
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
class UserEditForm(forms.ModelForm):
    """
    Form to allow user to edit their first name, last name and email
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    """
    Form to allow users to edit their profile photo
    """
    class Meta:
        model = Profile
        fields = ['photo']