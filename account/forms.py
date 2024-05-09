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
    github_url = forms.URLField(required=False, max_length=2000)
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
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data
    
class UserEditForm(forms.ModelForm):
    """
    Form to allow user to edit their first name, last name and email
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data

class ProfileEditForm(forms.ModelForm):
    """
    Form to allow users to edit their profile photo
    """
    class Meta:
        model = Profile
        fields = ['photo']