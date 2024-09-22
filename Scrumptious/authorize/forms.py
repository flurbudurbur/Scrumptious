from http.cookiejar import is_HDN

from django import forms
from authorize.models import Users

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'username', 'email', 'password']

    def __init__(self):
        super(UserRegistrationForm, self).__init__()
        self.fields['name'] = forms.CharField(max_length=100, widget=forms.TextInput())
        self.fields['username'] = forms.CharField(max_length=16, widget=forms.TextInput())
        self.fields['email'] = forms.EmailField(widget=forms.EmailInput())
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput())
        self.fields['confirm password'] = forms.CharField(widget=forms.PasswordInput())