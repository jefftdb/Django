from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Measure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)
    amount = models.CharField(max_length=65, null=True)
    measures = models.ForeignKey(Measure, on_delete=models.SET_NULL, null=True)
        
    def __str__(self):
        return self.amount +" "+ self.measures.name +" "+ self.name +"(s)"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    slug =  models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unity = models.CharField(max_length=65)
    servings_time = models.IntegerField()
    servings_unity = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='recipes/static/recipes/img')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient,related_name="ingredients")

    def __str__(self):
        return self.title
    
    def get_ingredients(self):
        return "\n".join([i.__str__() for i in self.ingredients.all()])




