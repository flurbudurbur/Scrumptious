from django import forms
from django.contrib.auth.decorators import login_required
from .models import Post

#login_required
class MakePost(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'ingredients', 'preparation', 'description', 'image']
        labels = {
            'title': 'Title',
            'ingredients': 'Ingredients',
            'preparation': 'Preparation',
            'description': 'Description',
            'image': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super(MakePost, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'p-2 border border-gray-300 rounded'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['ingredients'].widget.attrs['placeholder'] = 'Ingredients go here..'
        self.fields['preparation'].widget.attrs['placeholder'] = 'Preparation goes here..'
        self.fields['description'].widget.attrs['placeholder'] = 'Description goes here...'
        self.fields['image'].widget.attrs['placeholder'] = 'Image'
        self.fields['image'].widget.attrs['class'] = 'p-2 border border-gray-300 rounded'
        self.fields['image'].widget.attrs['accept'] = 'image/*'