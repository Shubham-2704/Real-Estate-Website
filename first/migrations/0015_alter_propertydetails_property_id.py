# Generated by Django 5.0.2 on 2024-03-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0014_propertydetails_property_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='property_id',
            field=models.CharField(max_length=100),
        ),
    ]
