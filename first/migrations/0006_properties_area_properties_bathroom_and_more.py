# Generated by Django 5.0.2 on 2024-03-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_remove_properties_amenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='area',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='properties',
            name='bathroom',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='properties',
            name='bedroom',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='properties',
            name='property_price',
            field=models.IntegerField(default=100000),
        ),
    ]
