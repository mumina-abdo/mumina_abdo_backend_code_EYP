# Generated by Django 5.0.7 on 2024-09-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_mymodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='created_at',
            field=models.DateTimeField(default='2024-09-22T08:47:30.103779+00:00'),
        ),
    ]