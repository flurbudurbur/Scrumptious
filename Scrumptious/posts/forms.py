from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

@login_required
class MakePost(forms.Form):
    title = forms.CharField(max_length=100)
    ingredient = forms.CharField(widget=forms.Textarea)
    preparation = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(MakePost, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'p-2 border border-gray-300 rounded'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['ingredient'].widget.attrs['placeholder'] = 'Ingredients go here..'
        self.fields['preparation'].widget.attrs['placeholder'] = 'Preparation goes here..'
        self.fields['description'].widget.attrs['placeholder'] = 'Description goes here...'
        self.fields['image'].widget.attrs['placeholder'] = 'Image'
        self.fields['image'].widget.attrs['class'] = 'p-2 border border-gray-300 rounded'
        self.fields['image'].widget.attrs['accept'] = 'image/*'