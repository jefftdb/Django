from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
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


@csrf_protect
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Formulário salvo com sucesso")
            return redirect('recipes:home')
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = RecipeForms()
    return render(request, 'recipes/pages/new_recipe.html', {'form': form})


def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeForms(instance=recipe)

    if request.method == 'POST':
        form = RecipeForms(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            print("Formulário editado com sucesso")
            return redirect('recipes:home')
        else:
            print("Formulário inválido")
            print(form.errors)

    return render(request, 'recipes/pages/edit_recipe.html', {'form': form, 'recipe_id': recipe_id})

def delete_recipe(request):
    pass


def login(request):
    pass
