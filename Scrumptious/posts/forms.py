from django import forms

from Scrumptious.models import Ingredients
from .models import Post, Comments, Likes


class MakePost(forms.ModelForm):
    # ingredients = forms.ModelChoiceField(
    #     queryset=Ingredients.objects.all().get('name'),
    #     widget=forms.SelectMultiple(attrs={'class': 'p-2 border border-gray-300 rounded'}),
    #     required=True
    # )

    class Meta:
        model = Post
        fields = ['title', 'preparation', 'description', 'image']
        labels = {
            'title': 'Title',
            'preparation': 'Preparation',
            'description': 'Description',
            'image': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super(MakePost, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'p-2 border border-gray-300 rounded'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        # self.fields['ingredients'].widget.attrs['placeholder'] = 'Ingredients go here..'
        # self.fields['ingredients'].widget.attrs['rows'] = 3
        self.fields['preparation'].widget.attrs['placeholder'] = 'Preparation goes here..'
        self.fields['preparation'].widget.attrs['rows'] = 3
        self.fields['description'].widget.attrs['placeholder'] = 'Description goes here...'
        self.fields['description'].widget.attrs['rows'] = 3
        self.fields['image'].widget.attrs['placeholder'] = 'Image'
        self.fields['image'].widget.attrs['class'] = 'p-2 border border-gray-300 rounded'
        self.fields['image'].widget.attrs['accept'] = 'image/*'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        labels = {
            'comment': 'Comment',
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'p-2 border border-gray-300 rounded'
        self.fields['comment'].widget.attrs['placeholder'] = 'Comment'
        self.fields['comment'].widget.attrs['rows'] = 3


class LikeForm(forms.ModelForm):
    class Meta:
        model = Likes
        fields = ['liked']
