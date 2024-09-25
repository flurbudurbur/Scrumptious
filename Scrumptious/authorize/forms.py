from django import forms
from authorize.models import Users


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']

    username = forms.CharField(max_length=16,
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Enter your username',
                                       'class': 'p-2 border border-gray-300 rounded',
                                   }
                               ),
                               label='Username',
                               required=True,
                               )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter your password',
            'class': 'p-2 border border-gray-300 rounded',
        }
    ),
        label='Password',
        required=True,
    )

    # def __init__(self):
    #     super(UserLoginForm, self).__init__()


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'username', 'email', 'password']

    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Enter your full name',
                                   'class': 'p-2 border border-gray-300 rounded',
                               }
                           ),
                           label='Full Name',
                           required=True,
                           )
    username = forms.CharField(max_length=16,
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Enter a username',
                                       'class': 'p-2 border border-gray-300 rounded',
                                   }
                               ),
                               label='Username',
                               required=True,
                               )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Enter your email address',
            'class': 'p-2 border border-gray-300 rounded',
        }
    ),
        label='Email',
        required=True,
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter a password',
            'class': 'p-2 border border-gray-300 rounded',
        }
    ),
        label='Password',
        required=True,
    )

    def __init__(self):
        super(UserRegistrationForm, self).__init__()
        self.fields['Confirm Password'] = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm your password',
                'class': 'p-2 border border-gray-300 rounded',
            }
        ),
            label='Confirm Password',
            required=True,
        )
