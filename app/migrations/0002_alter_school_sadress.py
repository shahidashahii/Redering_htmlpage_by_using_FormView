# Generated by Django 4.1.7 on 2023-05-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='Sadress',
            field=models.TextField(max_length=100),
        ),
    ]
