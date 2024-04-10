from django.contrib import admin
from recipes.models import Recipe,Measure,Ingredient,Category

class MeasureAdmin(admin.ModelAdmin):
    list_display = ("name","name")
    search_fields = ("name","name")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","name")
    search_fields = ("name","name")

class IngredientAdmin(admin.ModelAdmin):
       list_display = ("name","amount","measures")
       search_fields = ("name","name")

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title","description","slug","preparation_time","preparation_time_unity","servings_time",
                    "servings_unity","preparation_steps","preparation_steps_is_html","created_at","updated_at",
                    "is_published","cover","category","author","get_ingredients")
    search_fields = ("title","description","ingredients","category")
    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)

