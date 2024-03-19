from django.urls import path
from receitas import views

app_name = 'receitas'


urlpatterns = [
    path('',views.receitas),
    path('<int:id>', views.receita),
]