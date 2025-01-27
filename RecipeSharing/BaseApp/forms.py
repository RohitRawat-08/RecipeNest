from django import forms
from BaseApp.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields=['title','ingredients','instruction','catrgory']

