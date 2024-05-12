from django.shortcuts import render
from utills.recipes.factory import make_recipe
from recipes.models import Recipe

# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': Recipe.objects.all(),
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': Recipe.objects.get(id=id),
        'is_detail_page': True,
    })