# Generated by Django 5.1.1 on 2024-09-22 12:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0015_alter_shopping_list_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_list',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]