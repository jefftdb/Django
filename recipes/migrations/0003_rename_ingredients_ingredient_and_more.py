# Generated by Django 5.0.4 on 2024-04-09 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredients_measures_alter_category_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.RenameModel(
            old_name='Measures',
            new_name='Measure',
        ),
    ]