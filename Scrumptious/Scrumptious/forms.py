from django.forms import ModelForm

from Scrumptious.models import Ingredients


class AddIngredient(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name', 'created_by']