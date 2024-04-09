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
    path('', views.home, name="home"), # Home
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
