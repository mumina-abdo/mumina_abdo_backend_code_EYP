# Generated by Django 5.1.1 on 2024-09-17 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_remove_shopping_list_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_list',
            name='shopping_list_name',
        ),
    ]