# Generated by Django 5.0.2 on 2024-03-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_teamdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamdetails',
            name='team_profile',
            field=models.ImageField(upload_to='profileimages'),
        ),
    ]