# Generated by Django 5.0.2 on 2024-03-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0011_remove_propertydetails_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='property_price',
            field=models.CharField(max_length=25),
        ),
    ]
