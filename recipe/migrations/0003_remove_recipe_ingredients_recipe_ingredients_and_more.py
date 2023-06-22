# Generated by Django 4.0.2 on 2023-02-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_ingredient_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='Ingredients'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]