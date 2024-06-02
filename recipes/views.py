from django.shortcuts import render
from utills.recipes.factory import make_recipe
from recipes.models import Recipe
from .forms import RecipeForms

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

def new_recipe(request):
    
    if request.method == 'POST':
        form = RecipeForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = RecipeForms()
    else:
        form = RecipeForms()
    return render(request, 'recipes/pages/new_recipe.html', {'form':form})

def edit_recipe(request):
    pass

def delete_recipe(request):
    pass

def login(request):
    pass