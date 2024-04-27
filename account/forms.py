from django import forms

class LoginForm(forms.Form):
    """
    form to authenticate users
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)