from http.cookiejar import is_HDN

from django import forms
from authorize.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'p-2 border border-gray-300 rounded'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'p-2 border border-gray-300 rounded', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(
                attrs={'class': 'p-2 border border-gray-300 rounded', 'placeholder': 'Password'}),
        }
        fields = ['username', 'password']

    def __init__(self):
        super(UserRegistrationForm, self).__init__()
        self.fields['name'] = forms.CharField(max_length=100, widget=forms.TextInput())
        self.fields['username'] = forms.CharField(max_length=16, widget=forms.TextInput())
        self.fields['email'] = forms.EmailField(widget=forms.EmailInput())
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput())
        self.fields['confirm password'] = forms.CharField(widget=forms.PasswordInput())