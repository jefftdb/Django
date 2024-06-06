from django import forms
from .models import Recipe


class RecipeForms(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'slug', 
            'preparation_time', 
            'preparation_time_unity',
            'servings_time',
            'servings_unity',
            'preparation_steps',
            'cover',
            'category',
            'author',
            ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'preparation_time': forms.TextInput(attrs={'class': 'form-control'}),
            'preparation_time_unity': forms.TextInput(attrs={'class': 'form-control'}),
            'servings_time': forms.TextInput(attrs={'class': 'form-control'}),
            'servings_unity': forms.TextInput(attrs={'class': 'form-control'}),
            'preparation_steps': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
