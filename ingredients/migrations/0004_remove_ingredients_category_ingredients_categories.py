# Generated by Django 4.2.16 on 2024-09-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0005_category_updated_at_alter_category_name"),
        ("ingredients", "0003_remove_ingredients_category_delete_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredients",
            name="category",
        ),
        migrations.AddField(
            model_name="ingredients",
            name="categories",
            field=models.ManyToManyField(to="categories.category"),
        ),
    ]