from django.urls import path

from . import views


# cliente pede    servidor responde 
# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST

#def sobre(request):
#    return HttpResponse('Sobre')
    # return HTTP Response

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('new_recipe', views.new_recipe, name="new_recipe"),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name="delete_recipe"),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name="edit_recipe"),
    path('login', views.login, name="login"),
]
